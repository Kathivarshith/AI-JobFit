from src.skill_extractor import extract_skills


text = """
I have experience with Python, SQL, MySQL,
REST APIs, React.js, NLP, Machine Learning,
Scikit Learn and GitHub.
"""


skills = extract_skills(text)


print(skills)