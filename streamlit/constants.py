import streamlit as st
JD_PATH = "../jd_data/*"
RESUME_PATH = "../resume_data/*/*"
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
EMBEDDING_MODEL_NAME = "bert-base-uncased"
OUTPUT_PATH = "./output/"
JD_EMBEDDINGS_FILENAME = "jd_embeddings_large.pkl"
RESUME_EMBEDDINGS_FILENAME = "resume_embeddings_large.pkl"
IS_EMBEDDINGS_CREATED = True
GEMINI_MODEL_NAME = "gemini-1.5-flash"
TEMPLATE_CONTENT = """You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only 
respond once as 'assistant'. 

System Role: Resume Reviewer 

Your role is to act as a resume reviewer. You will assist users in improving their resumes to better align with specific 
job descriptions. Provide professional advice on resume building, interview preparation, and career development. 
Offer constructive feedback and encouragement. Whenever you are given a resume and a job description, there will be 
tokens added before and after the resume and job description. The tokens are as follows: <RESUME STARTS HERE> and 
<RESUME ENDS HERE> for the resume and <JOB DESCRIPTION STARTS HERE> and <JOB DESCRIPTION ENDS HERE> for the job 
description. Utilize these tokens to provide feedback and suggestions and clearly segregate the resume and job
description. Do not mix up the content of the resume and job description. In case the resume or job requirements 
in the description do not align with each other, do not mix up the content of the resume and job description and 
keep them separate and process them accordingly. Provide feedback based only on the content provided.
Strictly ONLY answer the question if it is relevant to resume and job description provided otherwise reply with 
'Please ask a relevant question'. Do not answer general knowledge questions.
"""

comparison_prompt = "Compare the resume: <RESUME STARTS HERE> {}. <RESUME ENDS HERE> with the job description: <JOB DESCRIPTION STARTS HERE> {}.<JOB DESCRIPTION ENDS HERE> Do they match? If not, what are the gaps? Do not make any assumptions about the candidate's skills or experience or the job requirements."
resume_analysis_prompt = "Provide a detailed summary of the candidate's skills, experience, and qualifications based on the content of the following resume: <RESUME STARTS HERE> {}. <RESUME ENDS HERE>"
job_description_analysis_prompt = "List the key skills, qualifications, and experience required as outlined in the following job description: <JOB DESCRIPTION STARTS HERE> {}. <JOB DESCRIPTION ENDS HERE>"
gap_analysis_prompt = "Compare the skills and experience detailed in this resume: <RESUME STARTS HERE> {} <RESUME ENDS HERE> with the requirements listed in the job description: <JOB DESCRIPTION STARTS HERE> {}. <JOB DESCRIPTION ENDS HERE> Identify any gaps or mismatches."
actionable_steps_prompt = "Given the gaps identified between the resume: <RESUME STARTS HERE> {} <RESUME ENDS HERE> and the job description: <JOB DESCRIPTION STARTS HERE> {} <JOB DESCRIPTION ENDS HERE>, suggest actionable steps for the candidate to acquire the necessary skills and experience."
experience_enhancement_prompt = "Based on the candidate's experience outlined in this resume: <RESUME STARTS HERE> {} <RESUME ENDS HERE>, recommend practical activities or steps to gain or improve the experience aligned with the needs of this role: <JOB DESCRIPTION STARTS HERE> {}. <JOB DESCRIPTION ENDS HERE>"
additional_qualifications_prompt = "For areas where this resume: <RESUME STARTS HERE> {} <RESUME ENDS HERE> falls short or does not satisfy the requirements of the job role : <JOB DESCRIPTION STARTS HERE> {} <JOB DESCRIPTION ENDS HERE>, suggest specific areas for improvement. Include recommendations for additional qualifications or certifications."
resume_tailoring_prompt = "Advise on how the candidate can tailor their resume: <RESUME STARTS HERE> {} <RESUME ENDS HERE> to align more closely with this job description: <JOB DESCRIPTION STARTS HERE> {} <JOB DESCRIPTION ENDS HERE>, focusing on emphasizing skills and experiences relevant to the job description."
relevant_skills_highlight_prompt = "Analyze this resume: <RESUME STARTS HERE> {} <RESUME ENDS HERE> and provide suggestions on restructuring it to foreground skills and experiences pertinent to the job description: <JOB DESCRIPTION STARTS HERE> {}. <JOB DESCRIPTION ENDS HERE>"
resume_formatting_prompt = "Offer guidance on how the candidate can enhance the formatting of their resume: <RESUME STARTS HERE> {} <RESUME ENDS HERE> to improve visual appeal and readability."
resume_length_prompt = "Recommend strategies for the candidate to adjust the length of their resume: <RESUME STARTS HERE> {} <RESUME ENDS HERE>, ensuring it is concise while remaining aligned with the requirements in the job description: <JOB DESCRIPTION STARTS HERE> {}. <JOB DESCRIPTION ENDS HERE>"
resume_edit_prompt = """Tailor this resume: <RESUME STARTS HERE> {} <RESUME ENDS HERE> to better match the job description: <JOB DESCRIPTION STARTS HERE> {}. <JOB DESCRIPTION ENDS HERE> Use the keywords from the job description to enhance the resume. Tailor the summary of resume according to job role. Tailor the skills section. Add relevant keywords from job decription in projects. Then print the resume section wise. Don't make bullet points too lengthy in job and project decription. Keep it short, precise and use key words. Start each bullet point with a strong action verb. Emphasize quantifiable results whenever possible. While not every bullet needs the full STAR method, try to incorporate its principles. Situation: Briefly set the context. Task: Describe your responsibility.
Action: Explain what you did.
Result: Highlight the positive outcome.
Conciseness: Keep bullet points concise and focused. Avoid overly long sentences.
Consistency: Maintain consistent verb tense and formatting throughout."""
