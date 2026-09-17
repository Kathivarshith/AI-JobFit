import streamlit as st
from src.resume_quality import analyze_resume_quality
from src.resume_parser import (
    extract_text_from_pdf,
    clean_text
)
from src.resume_recommendations import (
    generate_resume_recommendations
    )
from src.skill_extractor import extract_skills


st.title(" Resume Analyzer")

st.write(
    "Upload your resume and analyze the extracted content and skills."
)


# ============================================================
# SESSION STATE
# ============================================================

if "resume_text" not in st.session_state:
    st.session_state.resume_text = ""

if "cleaned_resume" not in st.session_state:
    st.session_state.cleaned_resume = ""

if "resume_skills" not in st.session_state:
    st.session_state.resume_skills = []


# ============================================================
# RESUME UPLOAD
# ============================================================

uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf"]
)


if uploaded_file is not None:

    st.success(
        f"Uploaded: {uploaded_file.name}"
    )


    # ========================================================
    # EXTRACT TEXT
    # ========================================================

    resume_text = extract_text_from_pdf(
        uploaded_file
    )


    # ========================================================
    # CLEAN TEXT
    # ========================================================

    cleaned_resume = clean_text(
        resume_text
    )


    # ========================================================
    # EXTRACT SKILLS
    # ========================================================

    resume_skills = extract_skills(
        cleaned_resume
    )

    resume_quality = analyze_resume_quality(
    cleaned_resume
    )

    st.session_state.resume_quality = resume_quality


    resume_recommendations = generate_resume_recommendations(
        resume_quality["missing_sections"],
        resume_quality["contact_information"]
    )

    st.session_state.resume_recommendations = (
        resume_recommendations
    )


    # ========================================================
    # SAVE DATA IN SESSION STATE
    # ========================================================

    st.session_state.resume_text = resume_text

    st.session_state.cleaned_resume = cleaned_resume

    st.session_state.resume_skills = resume_skills

    st.session_state.resume_name = uploaded_file.name


    # ========================================================
    # DISPLAY RESUME TEXT
    # ========================================================

    st.subheader(" Extracted Resume Text")

    st.text_area(
        "Resume Content",
        cleaned_resume,
        height=400
    )


    # ========================================================
    # DISPLAY SKILLS
    # ========================================================

    st.subheader(" Skills Detected")


    if resume_skills:

        st.success(
            f"{len(resume_skills)} skills detected"
        )

        for skill in resume_skills:

            st.write(
                f" {skill.title()}"
            )

    else:

        st.warning(
            "No supported technical skills detected."
        )

    #=======================================================

    st.divider()

    st.subheader("Resume Quality")

    quality_score = resume_quality["quality_score"]

    st.metric(
        "Resume Completeness",
        f"{quality_score}%"
    )


    st.subheader("Detected Sections")

    for section in resume_quality[
        "detected_sections"
    ]:

        st.write(
            section.title()
        )


    st.subheader("Missing Sections")

    if resume_quality["missing_sections"]:

        for section in resume_quality[
            "missing_sections"
        ]:

            st.write(
                section.title()
            )

    else:

        st.write(
            "No commonly expected sections are missing."
        )


    st.subheader("Contact Information")

    contact = resume_quality[
        "contact_information"
    ]

    for field, found in contact.items():

        status = "Found" if found else "Not detected"

        st.write(
            f"{field.title()}: {status}"
        )
    st.divider()

    st.subheader("Resume Improvement Recommendations")

    for recommendation in resume_recommendations:

        st.write(
            recommendation
        )

    # ========================================================
    # SUCCESS MESSAGE
    # ========================================================

    st.success(
        "Resume analysis completed! "
        "Go to the Job Matcher page."
    )