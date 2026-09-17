
import streamlit as st

from src.ai_advisor import get_ai_advice


# ============================================================
# PAGE TITLE
# ============================================================

st.title("AI Career Advisor")

st.write(
    "Get personalized resume and career recommendations "
    "based on your resume and the selected job description."
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
# CURRENT ANALYSIS
# ============================================================

st.subheader("Current Analysis")

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
        "Missing Skills",
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
        "No major missing skills detected."
    )


# ============================================================
# AI ADVISOR
# ============================================================

st.divider()

st.subheader("AI Career Analysis")

st.write(
    "The AI advisor will analyze your resume, job description, "
    "matched skills and missing skills."
)


if st.button(
    "Generate AI Analysis",
    key="generate_ai_analysis"
):

    with st.spinner(
        "Generating career analysis..."
    ):

        try:

            ai_result = get_ai_advice(

                resume_text=cleaned_resume,

                job_description=job_description,

                matched_skills=matched_skills,

                missing_skills=missing_skills,

                overall_score=overall_score

            )


            # =================================================
            # SAVE AI RESULT
            # =================================================

            st.session_state.ai_advice = ai_result


        except Exception as error:

            st.error(
                f"AI Advisor Error: {error}"
            )


# ============================================================
# DISPLAY AI RESULT
# ============================================================

if st.session_state.get("ai_advice"):

    st.divider()

    st.subheader(
        "AI Recommendations"
    )

    st.markdown(
        st.session_state.ai_advice
    )

