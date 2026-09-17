
import streamlit as st

from src.ai_advisor import get_interview_questions


# ============================================================
# PAGE TITLE
# ============================================================

st.title("AI Interview Coach")

st.write(
    "Prepare for interviews using your resume, job description, "
    "matched skills, and identified skill gaps."
)


# ============================================================
# CHECK RESUME
# ============================================================

if not st.session_state.get("cleaned_resume"):

    st.warning(
        "No resume found. Please upload your resume "
        "from the Resume Analyzer page first."
    )

    st.stop()


# ============================================================
# CHECK JOB ANALYSIS
# ============================================================

if not st.session_state.get("job_description"):

    st.warning(
        "No job description found. Please analyze a job "
        "from the Job Matcher page first."
    )

    st.stop()


# ============================================================
# GET DATA FROM SESSION STATE
# ============================================================

cleaned_resume = st.session_state.cleaned_resume

job_description = st.session_state.job_description

match_result = st.session_state.get(
    "match_result"
)

overall_score = st.session_state.get(
    "overall_score",
    0
)


# ============================================================
# VALIDATE MATCH RESULT
# ============================================================

if not match_result:

    st.warning(
        "No job matching analysis is available. "
        "Please run the Job Matcher first."
    )

    st.stop()


matched_skills = match_result.get(
    "matched_skills",
    []
)

missing_skills = match_result.get(
    "missing_skills",
    []
)


# ============================================================
# CURRENT JOB ANALYSIS
# ============================================================

st.subheader("Current Job Analysis")


col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "Overall Score",
        f"{overall_score}%"
    )


with col2:

    st.metric(
        "Matched Skills",
        len(matched_skills)
    )


with col3:

    st.metric(
        "Skill Gaps",
        len(missing_skills)
    )


# ============================================================
# MATCHED SKILLS
# ============================================================

st.subheader("Matched Skills")


if matched_skills:

    st.write(
        ", ".join(
            skill.title()
            for skill in matched_skills
        )
    )

else:

    st.write(
        "No matched skills detected."
    )


# ============================================================
# MISSING SKILLS
# ============================================================

st.subheader("Missing Skills")


if missing_skills:

    st.write(
        ", ".join(
            skill.title()
            for skill in missing_skills
        )
    )

else:

    st.write(
        "No major skill gaps detected."
    )


# ============================================================
# INTERVIEW PREPARATION
# ============================================================

st.divider()

st.subheader(
    "Generate Interview Questions"
)

st.write(
    "The AI coach will create technical, project-based, "
    "HR, and skill-gap questions based on your analysis."
)


if st.button(
    "Generate Interview Questions",
    key="generate_interview_questions"
):

    with st.spinner(
        "Preparing interview questions..."
    ):

        try:

            interview_result = get_interview_questions(

                resume_text=cleaned_resume,

                job_description=job_description,

                matched_skills=matched_skills,

                missing_skills=missing_skills,

                overall_score=overall_score

            )


            # =================================================
            # SAVE RESULT
            # =================================================

            st.session_state.interview_questions = (
                interview_result
            )


        except Exception as error:

            st.error(
                f"Interview Coach Error: {error}"
            )


# ============================================================
# DISPLAY INTERVIEW QUESTIONS
# ============================================================

if st.session_state.get(
    "interview_questions"
):

    st.divider()

    st.subheader(
        "Interview Preparation"
    )

    st.markdown(
        st.session_state.interview_questions
    )


# ============================================================
# PREPARATION SUMMARY
# ============================================================

st.divider()

st.subheader(
    "Preparation Focus"
)


if missing_skills:

    st.write(
        "Focus your preparation on the following skill gaps:"
    )

    for skill in missing_skills:

        st.write(
            skill.title()
        )

else:

    st.write(
        "Focus on explaining your projects, technical skills, "
        "and practical experience clearly."
    )


st.write(
    "During the interview, answer based on your actual "
    "knowledge and experience. Do not claim skills or "
    "experience that you do not have."
)
