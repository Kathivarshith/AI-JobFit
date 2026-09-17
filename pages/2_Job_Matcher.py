
import streamlit as st

from src.job_parser import analyze_job_description
from src.matcher import calculate_match
from src.text_similarity import calculate_text_similarity
from src.scoring import (
    calculate_overall_score,
    get_score_breakdown
)
from src.recommendation_engine import generate_recommendations


# ============================================================
# PAGE TITLE
# ============================================================

st.title(" Job Matcher")

st.write(
    "Compare your resume with a job description and identify "
    "your skills match, missing skills, and JobFit score."
)


# ============================================================
# CHECK RESUME
# ============================================================

if not st.session_state.get("cleaned_resume"):

    st.warning(
        " No resume found."
    )

    st.info(
        "Please go to the Resume Analyzer page, "
        "upload your resume, and come back here."
    )

    st.stop()


# ============================================================
# GET RESUME DATA
# ============================================================

cleaned_resume = st.session_state.cleaned_resume

resume_skills = st.session_state.resume_skills

resume_name = st.session_state.get(
    "resume_name",
    "Resume"
)


# ============================================================
# DISPLAY RESUME
# ============================================================

st.success(
    f"Resume loaded: {resume_name}"
)


st.subheader(" Resume Skills")


if resume_skills:

    for skill in resume_skills:

        st.write(
            f" {skill.title()}"
        )

else:

    st.warning(
        "No resume skills detected."
    )


# ============================================================
# JOB DESCRIPTION
# ============================================================

st.divider()

st.subheader(
    " Job Description"
)


job_description = st.text_area(
    "Paste the job description here",
    height=300,
    placeholder=(
        "Example:\n\n"
        "We are looking for a Python Developer "
        "with SQL, FastAPI, Git and Docker skills."
    )
)


# ============================================================
# ANALYZE JOB
# ============================================================

if st.button(
    " Analyze Job Match",
    key="analyze_job_button"
):

    if not job_description.strip():

        st.warning(
            "Please enter a job description."
        )

        st.stop()


    # ========================================================
    # JOB DESCRIPTION ANALYSIS
    # ========================================================

    job_result = analyze_job_description(
        job_description
    )

    job_skills = job_result["skills"]

    st.session_state.job_result = job_result

    st.subheader("Job Details")

    st.write(
        f"Job Title: {job_result['job_title']}"
    )

    st.write(
        f"Experience: {job_result['experience']}"
    )

    education = job_result["education"]

    if education:

        st.write(
            "Education: "
            + ", ".join(
                item.title()
                for item in education
            )
        )

    else:

        st.write(
            "Education: Not specified"
        )

    # ========================================================
    # CHECK JOB SKILLS
    # ========================================================

    if not job_skills:

        st.warning(
            "No supported technical skills were detected "
            "in this job description."
        )

        st.info(
            "Try a job description containing skills such as "
            "Python, SQL, MySQL, FastAPI, Git, Docker, etc."
        )

        st.stop()


    # ========================================================
    # SKILL MATCHING
    # ========================================================

    match_result = calculate_match(
        resume_skills,
        job_skills
    )


    skill_score = match_result[
        "match_score"
    ]


    # ========================================================
    # NLP SIMILARITY
    # ========================================================

    text_score = calculate_text_similarity(
        cleaned_resume,
        job_description
    )


    # ========================================================
    # OVERALL SCORE
    # ========================================================

    overall_score = calculate_overall_score(
        skill_score,
        text_score
    )

    score_breakdown = get_score_breakdown(
    skill_score,
    text_score
    )


    # ========================================================
    # RECOMMENDATIONS
    # ========================================================

    recommendations = generate_recommendations(
        match_result[
            "missing_skills"
        ]
    )


    # ========================================================
    # SAVE RESULTS TO SESSION STATE
    # ========================================================

    st.session_state.job_description = job_description

    st.session_state.job_skills = job_skills

    st.session_state.match_result = match_result

    st.session_state.skill_score = skill_score

    st.session_state.text_score = text_score

    st.session_state.overall_score = overall_score

    st.session_state.recommendations = recommendations


    # ========================================================
    # REQUIRED JOB SKILLS
    # ========================================================

    st.divider()

    st.subheader(
        " Required Job Skills"
    )


    for skill in job_skills:

        st.write(
            f"🔹 {skill.title()}"
        )

    #====

    st.subheader("Preferred Skills")

    preferred_skills = job_result[
        "preferred_skills"
    ]

    if preferred_skills:

        st.write(
            ", ".join(
                skill.title()
                for skill in preferred_skills
            )
        )

    else:

        st.write(
            "No preferred skills detected."
        )


    st.subheader("Responsibilities")

    responsibilities = job_result[
        "responsibilities"
    ]

    if responsibilities:

        for responsibility in responsibilities:

            st.write(
                responsibility
            )

    else:

        st.write(
            "Responsibilities could not be automatically detected."
        )




    # ========================================================
    # SCORE
    # ========================================================

    st.divider()

    st.subheader(
        " JobFit Score"
    )


    col1, col2, col3 = st.columns(3)


    st.subheader("Score Breakdown")

    st.write(
        f"Skill Match Contribution: "
        f"{score_breakdown['skill_contribution']}%"
    )

    st.write(
        f"Text Similarity Contribution: "
        f"{score_breakdown['text_contribution']}%"
    )

    st.write(
        f"Skill Weight: "
        f"{score_breakdown['skill_weight'] * 100:.0f}%"
    )

    st.write(
        f"Text Weight: "
        f"{score_breakdown['text_weight'] * 100:.0f}%"
    )
    


    with col1:

        st.metric(
            "Skill Match",
            f"{skill_score}%"
        )


    with col2:

        st.metric(
            "NLP Similarity",
            f"{text_score}%"
        )


    with col3:

        st.metric(
            "Overall Score",
            f"{overall_score}%"
        )


    # ========================================================
    # MATCHED SKILLS
    # ========================================================

    st.subheader(
        " Matched Skills"
    )


    if match_result["matched_skills"]:

        for skill in match_result[
            "matched_skills"
        ]:

            st.write(
                f" {skill.title()}"
            )

    else:

        st.info(
            "No matching skills found."
        )


    # ========================================================
    # MISSING SKILLS
    # ========================================================

    st.subheader(
        " Missing Skills"
    )


    if match_result["missing_skills"]:

        for skill in match_result[
            "missing_skills"
        ]:

            st.write(
                f" {skill.title()}"
            )

    else:

        st.success(
            "No major missing skills detected!"
        )


    # ========================================================
    # ADDITIONAL SKILLS
    # ========================================================

    st.subheader(
        " Additional Resume Skills"
    )


    if match_result["extra_skills"]:

        for skill in match_result[
            "extra_skills"
        ]:

            st.write(
                f" {skill.title()}"
            )

    else:

        st.info(
            "No additional skills detected."
        )


    # ========================================================
    # LEARNING RECOMMENDATIONS
    # ========================================================

    st.divider()

    st.subheader(
        " Learning Recommendations"
    )


    if recommendations:

        for item in recommendations:

            with st.expander(
                item["skill"].upper()
            ):

                st.write(
                    f" Learn: {item['learn']}"
                )

                st.write(
                    f" Project: {item['project']}"
                )

                st.write(
                    f" Interview Topics: "
                    f"{item['interview']}"
                )

    else:

        st.info(
            "No specific learning recommendations available."
        )


    # ========================================================
    # STATUS
    # ========================================================

    st.success(
        " Job analysis completed successfully!"
    )


# ============================================================
# SHOW PREVIOUS RESULT
# ============================================================

elif st.session_state.get("match_result"):

    st.divider()

    st.subheader(
        " Previous Analysis"
    )


    previous_result = st.session_state.match_result

    previous_skill_score = st.session_state.get(
        "skill_score",
        0
    )

    previous_text_score = st.session_state.get(
        "text_score",
        0
    )

    previous_overall_score = st.session_state.get(
        "overall_score",
        0
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Skill Match",
            f"{previous_skill_score}%"
        )


    with col2:

        st.metric(
            "NLP Similarity",
            f"{previous_text_score}%"
        )


    with col3:

        st.metric(
            "Overall Score",
            f"{previous_overall_score}%"
        )


    st.subheader(
        " Matched Skills"
    )


    for skill in previous_result[
        "matched_skills"
    ]:

        st.write(
            f" {skill.title()}"
        )


    st.subheader(
        " Missing Skills"
    )


    for skill in previous_result[
        "missing_skills"
    ]:

        st.write(
            f" {skill.title()}"
        )
