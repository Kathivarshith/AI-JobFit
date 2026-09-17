from src.interview_coach import build_interview_prompt


prompt = build_interview_prompt(

    resume_text="""
    Python developer with SQL, Pandas and Streamlit experience.
    Built machine learning projects.
    """,

    job_description="""
    Python Developer required.
    Skills: Python, SQL, FastAPI, Docker and Git.
    """,

    matched_skills=[
        "python",
        "sql",
        "git"
    ],

    missing_skills=[
        "fastapi",
        "docker"
    ],

    overall_score=72.5
)


print(prompt)