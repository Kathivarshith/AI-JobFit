
import streamlit as st

from src.database import (
    get_analysis_history
)


# ============================================================
# PAGE TITLE
# ============================================================

st.title("Analysis History")

st.write(
    "View your previously saved resume and job matching analyses."
)


# ============================================================
# GET HISTORY
# ============================================================

history = get_analysis_history()


# ============================================================
# CHECK HISTORY
# ============================================================

if not history:

    st.info(
        "No previous analyses found."
    )

    st.write(
        "Run a job analysis and use the Save Analysis button "
        "to create your first history record."
    )

    st.stop()


# ============================================================
# SUMMARY
# ============================================================

total_analyses = len(history)

average_score = sum(
    row[4]
    for row in history
) / total_analyses


st.subheader("Summary")


col1, col2 = st.columns(2)


with col1:

    st.metric(
        "Total Analyses",
        total_analyses
    )


with col2:

    st.metric(
        "Average JobFit Score",
        f"{average_score:.2f}%"
    )


# ============================================================
# ANALYSIS RECORDS
# ============================================================

st.divider()

st.subheader("Previous Analyses")


for row in history:

    (
        analysis_id,
        resume_name,
        skill_score,
        text_score,
        overall_score,
        matched_skills,
        missing_skills,
        created_at
    ) = row


    with st.expander(
        f"Analysis #{analysis_id} - {resume_name}"
    ):

        st.write(
            f"Date: {created_at}"
        )

        st.write(
            f"Skill Match: {skill_score}%"
        )

        st.write(
            f"NLP Similarity: {text_score}%"
        )

        st.write(
            f"Overall JobFit Score: {overall_score}%"
        )


        st.subheader(
            "Matched Skills"
        )


        if matched_skills:

            st.write(
                matched_skills
            )

        else:

            st.write(
                "No matched skills."
            )


        st.subheader(
            "Missing Skills"
        )


        if missing_skills:

            st.write(
                missing_skills
            )

        else:

            st.write(
                "No missing skills."
            )

