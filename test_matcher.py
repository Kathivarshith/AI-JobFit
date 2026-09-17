from src.matcher import calculate_match


resume_skills = [
    "python",
    "sql",
    "pandas",
    "git",
    "mysql"
]


job_skills = [
    "python",
    "sql",
    "pandas",
    "fastapi",
    "docker",
    "git"
]


result = calculate_match(resume_skills, job_skills)


print("Match Score:", result["match_score"])

print("\nMatched Skills:")
for skill in result["matched_skills"]:
    print("-", skill)

print("\nMissing Skills:")
for skill in result["missing_skills"]:
    print("-", skill)

print("\nExtra Skills:")
for skill in result["extra_skills"]:
    print("-", skill)
    