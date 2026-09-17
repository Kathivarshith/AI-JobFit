from src.job_parser import analyze_job_description


job_description = """
We are looking for a Python Developer.

Requirements:
Python
SQL
Pandas
FastAPI
REST API
Docker
Git
MySQL
"""


result = analyze_job_description(job_description)

print("Required Skills:")

for skill in result["skills"]:
    print("-", skill)