# Resume Analyzer with LLM (Gemini)

This project is a Streamlit application that utilizes Google's Gemini LLM to analyze resumes against job descriptions, providing tailored feedback and improvement suggestions.

## Description

This application automates the process of resume review by:

* **Analyzing Resumes:** Extracting relevant information from uploaded resumes.
* **Comparing with Job Descriptions:** Comparing the resume content against provided job descriptions.
* **Providing Feedback:** Generating personalized feedback, including skill gap analysis, actionable suggestions, and resume formatting tips.
* **Leveraging Gemini LLM:** Using the power of Google's Gemini API to generate intelligent and insightful feedback.

## Features

* **Resume Upload:** Users can upload resume files.
* **Job Description Input:** Users can input job descriptions.
* **Automated Analysis:** The application automatically analyzes the resume and job description.
* **Detailed Report:** Generates a comprehensive report with feedback and suggestions.
* **Skill Gap Analysis:** Highlights areas where the resume falls short of the job requirements.
* **Actionable Suggestions:** Provides specific recommendations for improving the resume.
* **Resume Formatting Tips:** Offers guidance on optimizing resume formatting.

## Technologies Used

* **Google Gemini API:** Provides intelligent text analysis and generation for resume evaluation, feedback, and skill gap analysis.
* **Langchain:** For orchestrating and managing the interactions with Large Language Models (LLMs), streamlining prompt engineering, response handling, and complex workflow integration.
* **Hugging Face Transformers (BERT):** Used for generating text embeddings, enabling semantic similarity comparisons between resumes and job descriptions.
* **Streamlit:** For building the interactive web application interface, enabling easy deployment and user interaction, specifically for the chat application feature.
* **Python:** The primary programming language, providing the flexibility and extensive libraries necessary for data processing, LLM integration, application logic, and OCR implementation.
* **OCR (Optical Character Recognition):** Implemented using the Tesseract library, enabling the extraction of text from image-based resumes.
* **Git:** For version control, facilitating collaboration and tracking changes throughout the project's development.


## Setup

1.  **Clone the Repository:**

    ```bash
    git clone [https://github.com/anaynasingh/resume-analyzer-with-llm-gemini.git](https://www.google.com/search?q=https://github.com/anaynasingh/resume-analyzer-with-llm-gemini.git)
    cd resume-analyzer-with-llm-gemini
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate      # On Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Streamlit Secrets:**

    * Create a `.streamlit/secrets.toml` file (if you are running locally) or add secrets directly to your Streamlit Cloud app settings.
    * Add your Google Gemini API key:

        ```toml
        GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
        ```

5.  **Run the Application:**

    ```bash
    streamlit run streamlit/resume_suggestions.py
    ```


## Contributing

Contributions are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.


