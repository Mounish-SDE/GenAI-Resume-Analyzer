# GenAI Resume Analyzer

A beginner-friendly Streamlit app that compares a resume PDF with a job description using the Gemini API.

## Features
- Upload a text-based PDF resume
- Paste a job description
- Get strengths, gaps, truthful ATS keyword suggestions, bullet rewrites, a 7-day plan, and interview prep
- Download the analysis as Markdown

## Requirements
- Python 3.10+
- A Gemini API key from Google AI Studio
- Internet access while using the app

## Run locally

1. Extract this project ZIP.
2. Open a terminal in the project folder.
3. Create and activate a virtual environment:

   Windows:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   macOS/Linux:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Copy `.env.example` to `.env` and set your API key:
   ```env
   GEMINI_API_KEY=your_real_key
   ```

6. Start the app:
   ```bash
   streamlit run app.py
   ```

## GitHub upload
- Create a new GitHub repository named `genai-resume-analyzer`.
- Upload `app.py`, `requirements.txt`, `README.md`, `.gitignore`, and `.env.example`.
- **Never upload `.env` or your API key.**
- Add screenshots after running the app.
- Include your own contribution and explain the code in interviews.

## Limitations
- This is a project/demo, not an ATS system or hiring prediction.
- PDF extraction works best with selectable text; scanned PDFs need OCR.
- AI output can be wrong. Verify all suggestions and never add skills or metrics you cannot substantiate.
- The app sends resume text to the Gemini API. Review provider privacy terms before using personal documents.

- **PROJECT DEMOS**

- GenAI Resume Analyzer: https://genai-resume-analyzer000.streamlit.app/

