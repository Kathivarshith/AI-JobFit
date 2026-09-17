from src.ai_advisor import build_ai_prompt


prompt = build_ai_prompt(
    "Python developer with SQL and Pandas experience.",
    "Looking for Python developer with Python, SQL, FastAPI and Docker.",
    ["python", "sql"],
    ["fastapi", "docker"],
    72.5
)


print(prompt)
