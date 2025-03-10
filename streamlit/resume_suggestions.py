# Description: Streamlit app for generating resume suggestions based on a job description.
# The app allows users to upload their resume and a job description, and provides detailed insights and actionable suggestions to improve the resume.
import os
import openai
import streamlit as st
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from streamlit_feedback import streamlit_feedback
from constants import (
    OPENAI_API_KEY, TEMPLATE_CONTENT, comparison_prompt, resume_analysis_prompt,
    job_description_analysis_prompt, gap_analysis_prompt, actionable_steps_prompt, experience_enhancement_prompt,
    additional_qualifications_prompt, resume_tailoring_prompt, relevant_skills_highlight_prompt,
    resume_formatting_prompt, resume_length_prompt, resume_edit_prompt
)
from directory_reader import DirectoryReader

# Set up OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set up Streamlit page
st.set_page_config(page_title="Resume Analyser")

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your personal resume reviewer. Upload your resume and job description, and I'll provide insights to help you land your dream job. You can select from the following options to get started or provide your own prompt."}
    ]

# Sidebar for file uploads
with st.sidebar:
    st.title('Resume Analyser')
    st.write("Upload your resume and JD for my recommendations.")
    resume_file = st.file_uploader("Upload your resume (pdf file only)", type=["pdf"])
    jd_file = st.file_uploader("Upload your JD (txt file only)", type=["txt"])

# Extract content from uploaded files
resume_content = None
job_description_content = None

if resume_file is not None and jd_file is not None:
    directory_reader = DirectoryReader("", "")
    resume_content = directory_reader.extract_text_from_pdf(resume_file)
    if jd_file.type == 'text/plain':
        from io import StringIO
        stringio = StringIO(jd_file.getvalue().decode('utf-8'))
        job_description_content = stringio.read()

# System prompt for the chatbot
SYSTEM_PROMPT = "\n\n" + TEMPLATE_CONTENT + "<RESUME STARTS HERE> {}. <RESUME ENDS HERE> with the job description: <JOB DESCRIPTION STARTS HERE> {}.<JOB DESCRIPTION ENDS HERE>\n\nBe crisp and clear in response. DO NOT provide the resume and job description in the response\n\n".format(resume_content, job_description_content)

# Function to generate a response using OpenAI's API
def generate_response(prompt_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini-2024-07-18",  # Use GPT-4o mini model
            messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": prompt_input}],
            temperature=0.0
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {e}"

# Function to display the four buttons as part of the chatbot's message
def display_buttons():
    st.markdown("**Please choose one of the following options or provide your own prompt:**")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📄 Tailor Resume Based on Job Description"):
            st.session_state.button_clicked = "Generate New Resume"
        if st.button("📄 Detailed Report"):
            st.session_state.button_clicked = "Detailed Report"
        if st.button("📌 Actionable Suggestions"):
            st.session_state.button_clicked = "Actionable Suggestions"
    with col2:
        if st.button("📊 Skill Gap Analysis"):
            st.session_state.button_clicked = "Skill Gap Analysis"
        if st.button("🔍 Strengths & Weaknesses"):
            st.session_state.button_clicked = "Strengths & Weaknesses"
        if st.button("📝 Generate Cover Letter"):
            st.session_state.button_clicked = "Generate Cover Letter"

# Function to generate a detailed report
def generate_report():
    if not resume_content or not job_description_content:
        st.warning("Please upload both a resume and a job description before generating the report.")
        return

    with st.spinner("Generating report..."):
        comparison_analysis = generate_response(comparison_prompt.format(resume_content, job_description_content))
        resume_analysis = generate_response(resume_analysis_prompt.format(resume_content))
        job_description_analysis = generate_response(job_description_analysis_prompt.format(job_description_content))
        gap_analysis = generate_response(gap_analysis_prompt.format(resume_content, job_description_content))
        actionable_steps_analysis = generate_response(actionable_steps_prompt.format(resume_content, job_description_content))
        experience_enhancement_analysis = generate_response(experience_enhancement_prompt.format(resume_content, job_description_content))
        additional_qualifications_analysis = generate_response(additional_qualifications_prompt.format(resume_content, job_description_content))
        resume_tailoring_analysis = generate_response(resume_tailoring_prompt.format(resume_content, job_description_content))
        relevant_skills_highlight_analysis = generate_response(relevant_skills_highlight_prompt.format(resume_content, job_description_content))
        resume_formatting_analysis = generate_response(resume_formatting_prompt.format(resume_content, job_description_content))
        resume_length_analysis = generate_response(resume_length_prompt.format(resume_content, job_description_content))

        report = f"**Comparison Analysis:**\n{comparison_analysis}\n\n" \
                 f"**Resume Analysis:**\n{resume_analysis}\n\n" \
                 f"**Job Description Analysis:**\n{job_description_analysis}\n\n" \
                 f"**Gap Analysis:**\n{gap_analysis}\n\n" \
                 f"**Actionable Steps:**\n{actionable_steps_analysis}\n\n" \
                 f"**Experience Enhancement:**\n{experience_enhancement_analysis}\n\n" \
                 f"**Additional Qualifications:**\n{additional_qualifications_analysis}\n\n" \
                 f"**Resume Tailoring:**\n{resume_tailoring_analysis}\n\n" \
                 f"**Relevant Skills Highlight:**\n{relevant_skills_highlight_analysis}\n\n" \
                 f"**Resume Formatting:**\n{resume_formatting_analysis}\n\n" \
                 f"**Resume Length:**\n{resume_length_analysis}"

        st.session_state.messages.append({"role": "assistant", "content": report})

# Function to generate a new resume based on job description
def generate_new_resume():
    if not resume_content or not job_description_content:
        st.warning("Please upload both a resume and a job description before generating the report.")
        return

    with st.spinner("Generating new resume..."):
        gap_analysis = generate_response(gap_analysis_prompt.format(resume_content, job_description_content))
        new_resume = generate_response(resume_edit_prompt.format(resume_content, job_description_content))
        st.session_state.messages.append({"role": "assistant", "content": f"**New Resume Based on Job Description:**\n\n{new_resume}"})

def generate_cover_letter():
    if not resume_content or not job_description_content:
        st.warning("Please upload both a resume and a job description before generating the cover letter.")
        return

    with st.spinner("Generating cover letter..."):
        cover_letter_prompt = f"Generate a professional cover letter based on the following resume and job description:\n\nResume:\n{resume_content}\n\nJob Description:\n{job_description_content}\n\nThe cover letter should be tailored to the job role, highlighting relevant skills and experience.Include details like name, address, email, phone number, linkedin, github, personal portfolio etc from resume if provided. Add details of address of company, hiring manager name, company name, job title, company address, city, state, zip code from job decription. set date as the current date. The cover letter should be concise, engaging, and professional."
        cover_letter = generate_response(cover_letter_prompt)
        st.session_state.messages.append({"role": "assistant", "content": f"**Generated Cover Letter:**\n\n{cover_letter}"})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        if message["role"] == "assistant" and len(st.session_state.messages) == 1:
            display_buttons()

# Handle button clicks
if "button_clicked" in st.session_state:
    if st.session_state.button_clicked == "Detailed Report":
        generate_report()
    elif st.session_state.button_clicked == "Actionable Suggestions":
        prompt = actionable_steps_prompt.format(resume_content, job_description_content)
        result = generate_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": result})
    elif st.session_state.button_clicked == "Skill Gap Analysis":
        prompt = gap_analysis_prompt.format(resume_content, job_description_content)
        result = generate_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": result})
    elif st.session_state.button_clicked == "Strengths & Weaknesses":
        prompt = resume_analysis_prompt.format(resume_content)
        result = generate_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": result})
    elif st.session_state.button_clicked == "Generate New Resume":
        generate_new_resume()
    elif st.session_state.button_clicked == "Generate Cover Letter":
        generate_cover_letter()

    # Clear the button state and trigger a UI refresh
    del st.session_state.button_clicked
    st.rerun()  # Force Streamlit to refresh immediately after processing the button click

# User-provided prompt
if prompt := st.chat_input():
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message immediately
    with st.chat_message("user"):
        st.write(prompt)

    # Generate response and display it immediately
    response = generate_response(prompt + SYSTEM_PROMPT)
    with st.chat_message("assistant"):
        st.write(response)

    # Append response to session state
    st.session_state.messages.append({"role": "assistant", "content": response})
