# 🤖 AI JobFit — AI Resume Analyzer & Interview Coach

AI JobFit is an AI-powered career assistant built with **Python and Streamlit** that helps job seekers analyze their resumes against job descriptions, identify skill gaps, improve their resumes, and prepare for interviews.

## 🚀 Live Demo

👉 **[Launch AI JobFit](https://ai-jobfit-1114.streamlit.app/)**

Try the application directly in your browser.

---

## 📌 Features

* 📄 **Resume PDF Analysis** — Upload and extract content from your resume.
* 🎯 **Job Fit Analysis** — Compare your resume with a target job description.
* 📊 **Skill Gap Detection** — Identify matching and missing skills.
* 🤖 **AI Resume Analysis** — Get personalized improvement recommendations.
* 🎤 **Interview Coach** — Generate role-specific interview questions.
* 💡 **Career Recommendations** — Get actionable suggestions based on your resume and target role.
* ☁️ **Cloud Deployment** — Deployed using Streamlit Community Cloud.

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **AI / LLM API**
* **PDF Parsing**
* **NLP / Text Processing**
* **Git & GitHub**
* **Streamlit Community Cloud**

---

## 🏗️ Project Architecture

```text
AI-JobFit/
│
├── app.py
│
├── src/
│   ├── resume_parser.py
│   ├── resume_analyzer.py
│   ├── interview_coach.py
│   └── ...
│
├── assets/
│   └── ...
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Application Workflow

```text
Resume PDF
    │
    ▼
PDF Text Extraction
    │
    ▼
Text Cleaning & Processing
    │
    ├───────────────┐
    ▼               ▼
Resume Analysis   Job Description
    │               │
    └───────┬───────┘
            ▼
      Job Fit Analysis
            │
            ▼
       Skill Gap Analysis
            │
            ▼
      AI Recommendations
            │
            ▼
      Interview Coach
            │
            ▼
   Role-Specific Questions
```

---

## 🔑 API Configuration

The AI features require an API key.

For **Streamlit Cloud**, configure the API key through:

**App → Settings → Secrets**

Example:

```toml
API_KEY = "your_api_key_here"
```

⚠️ **Never commit your real API key to GitHub.**

Add sensitive files to `.gitignore`:

```gitignore
.env
.streamlit/secrets.toml
__pycache__/
*.pyc
```

---

## 💻 Run Locally

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project:

```bash
cd AI-JobFit
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 🎯 Use Cases

AI JobFit is designed for:

* Fresh graduates
* Students
* Job seekers
* Career switchers
* Candidates targeting specific job descriptions
* Interview preparation

---

## 🧠 Key Learning Outcomes

This project provided hands-on experience with:

* Python development
* Streamlit application development
* PDF text extraction
* NLP and text processing
* AI/LLM API integration
* Prompt-based AI workflows
* Resume analysis
* Job-description matching
* Skill-gap analysis
* API secret management
* GitHub version control
* Cloud deployment

---

## 👨‍💻 Author

**Kathi Varshith**

B.Tech — Electronics & Communication Engineering

📍 Hyderabad, India

🌐 **Portfolio:** https://kathivarshith.netlify.app/

💼 **LinkedIn:** https://www.linkedin.com/in/kathi-varshith1114/

---

## ⭐ Project

If you find **AI JobFit** useful, consider giving the repository a ⭐ on GitHub.

---

## 📄 License

This project is created for educational, portfolio, and demonstration purposes.
