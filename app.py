import os
import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader
from google import genai

load_dotenv()
st.set_page_config(page_title="GenAI Resume Analyzer", page_icon="📄", layout="centered")
st.title("📄 GenAI Resume Analyzer")
st.caption("Compare a resume with a job description and get actionable feedback.")

api_key = os.getenv("GEMINI_API_KEY", "").strip()
if not api_key:
    st.warning("Add your Gemini API key to a .env file. See the README.")
    st.stop()

client = genai.Client(api_key=api_key)

def extract_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    pages = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n".join(pages).strip()


def analyze(resume_text, job_text):
    prompt = f"""
You are a career coach and resume reviewer.
Analyze the resume against the job description.

Use only evidence in the supplied text.
Do not invent experience, skills, metrics, or credentials.

Return clear Markdown with:
1. Overall fit
2. Relevant strengths
3. Missing or weakly evidenced requirements
4. Resume bullet improvements
5. Truthful ATS keyword suggestions
6. A 7-day improvement plan
7. Interview questions

Keep feedback constructive and suitable for a student/intern.

RESUME:
{resume_text[:25000]}

JOB DESCRIPTION:
{job_text[:15000]}
"""

    import time

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt,
            )

            return response.text or "The model returned no text."

        except Exception as exc:
            error_message = str(exc)

            if attempt == 2:
                raise RuntimeError(
                    f"Gemini API failed after 3 attempts: {error_message}"
                ) from exc

            if "503" in error_message or "UNAVAILABLE" in error_message:
                time.sleep(2 ** (attempt + 1))
            else:
                raise

with st.form("analysis_form"):
    resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    job_description = st.text_area("Paste the job description", height=250,
        placeholder="Paste the role, responsibilities, skills, and eligibility details here.")
    submitted = st.form_submit_button("Analyze resume", type="primary")

if submitted:
    if not resume_file:
        st.error("Please upload a PDF resume.")
    elif not job_description.strip():
        st.error("Please paste the job description.")
    else:
        try:
            resume_text = extract_pdf(resume_file)
            if not resume_text:
                st.error("No selectable text found. Try exporting your resume as a text-based PDF.")
            else:
                with st.spinner("Analyzing your resume..."):
                    result = analyze(resume_text, job_description)
                st.subheader("Analysis")
                st.markdown(result)
                st.download_button("Download analysis as Markdown", result,
                                 file_name="resume_analysis.md", mime="text/markdown")
        except Exception as exc:
            st.error("Analysis failed. Check your API key, internet connection, and quota.")
            st.caption(str(exc))

st.divider()
st.caption("Privacy note: resume text is sent to the configured Gemini API for analysis. Avoid uploading sensitive information you do not want processed.")
