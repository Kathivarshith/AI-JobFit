from src.resume_advisor import generate_resume_advice


missing_skills = [
    "fastapi",
    "docker"
]

matched_skills = [
    "python",
    "sql",
    "pandas"
]

overall_score = 62.5


advice = generate_resume_advice(
    missing_skills,
    matched_skills,
    overall_score
)


for item in advice:
    print("💡", item)