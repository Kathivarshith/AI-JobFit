import sqlite3


DATABASE_NAME = "jobfit.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)

    return connection


def create_table():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            resume_name TEXT,

            job_description TEXT,

            skill_score REAL,

            text_score REAL,

            overall_score REAL,

            matched_skills TEXT,

            missing_skills TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    connection.commit()

    connection.close()



def save_analysis(
    resume_name,
    job_description,
    skill_score,
    text_score,
    overall_score,
    matched_skills,
    missing_skills
):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO analyses (
            resume_name,
            job_description,
            skill_score,
            text_score,
            overall_score,
            matched_skills,
            missing_skills
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        resume_name,
        job_description,
        skill_score,
        text_score,
        overall_score,
        ", ".join(matched_skills),
        ", ".join(missing_skills)
    ))

    connection.commit()

    connection.close()  

if __name__ == "__main__":

    create_table()

    save_analysis(
        "resume.pdf",
        "Python Developer with SQL and Docker",
        75.0,
        68.5,
        73.05,
        ["python", "sql"],
        ["docker"]
    )

    print("Analysis saved successfully!")

def get_analysis_history():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            resume_name,
            skill_score,
            text_score,
            overall_score,
            matched_skills,
            missing_skills,
            created_at
        FROM analyses
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    connection.close()

    return rows

if __name__ == "__main__":

    create_table()

    history = get_analysis_history()

    print("Analysis History:")

    for row in history:
        print(row)