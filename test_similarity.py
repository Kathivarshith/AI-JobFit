from src.text_similarity import calculate_text_similarity


resume = """
Python developer with experience building web applications.
Worked with SQL, Pandas, REST APIs and Streamlit.
Developed machine learning projects using Python.
"""


job = """
We are looking for a Python developer.
The candidate should have experience with backend applications,
Python APIs, SQL databases and web development.
"""


score = calculate_text_similarity(
    resume,
    job
)


print("Text Similarity:", score, "%")
