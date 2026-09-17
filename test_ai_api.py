from src.ai_advisor import get_ai_advice


resume = """
Python developer with experience in Python, SQL,
Pandas and Streamlit. Built machine learning projects.
"""


job = """
We are looking for a Python developer with Python,
SQL, FastAPI and Docker experience.
"""


result = get_ai_advice(
    resume_text=resume,
    job_description=job,
    matched_skills=["python", "sql"],
    missing_skills=["fastapi", "docker"],
    overall_score=72.5
)


print(result)