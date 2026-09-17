import streamlit as st


st.set_page_config(
    page_title="AI JobFit",
    page_icon=None,
    layout="wide"
)


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

session_defaults = {
    "resume_text": "",
    "cleaned_resume": "",
    "resume_skills": [],
    "resume_name": "",
    "resume_quality": {},
    "resume_recommendations": [],
    "job_description": "",
    "job_skills": [],
    "job_result": None,
    "match_result": None,
    "skill_score": 0,
    "text_score": 0,
    "overall_score": 0,
    "recommendations": [],
    "ai_advice": "",
    "interview_questions": ""
}


for key, default_value in session_defaults.items():

    if key not in st.session_state:
        st.session_state[key] = default_value


# ---------------------------------------------------------
# HOME
# ---------------------------------------------------------

st.title("AI JobFit")

st.subheader(
    "AI-Powered Resume and Job Matching System"
)

st.write(
    "Analyze your resume, compare it with job descriptions, "
    "identify skill gaps, receive personalized recommendations, "
    "and prepare for interviews."
)


# ---------------------------------------------------------
# WORKFLOW
# ---------------------------------------------------------

st.divider()

st.header("How AI JobFit Works")

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.subheader("Resume Analysis")

    st.write(
        "Upload a PDF resume and extract resume content, "
        "skills, sections, and contact information."
    )


with col2:

    st.subheader("Job Analysis")

    st.write(
        "Paste a job description and detect the job title, "
        "experience, education, required skills, preferred "
        "skills, and responsibilities."
    )


with col3:

    st.subheader("Job Matching")

    st.write(
        "Compare the detected job requirements with the "
        "skills detected in your resume."
    )


with col4:

    st.subheader("AI Preparation")

    st.write(
        "Get career recommendations and personalized "
        "interview preparation."
    )


# ---------------------------------------------------------
# CURRENT STATUS
# ---------------------------------------------------------

st.divider()

st.header("Current Analysis")


resume_available = bool(
    st.session_state.cleaned_resume
)

job_available = bool(
    st.session_state.job_description
)

analysis_available = (
    st.session_state.match_result is not None
)


col1, col2, col3 = st.columns(3)


with col1:

    if resume_available:

        st.success("Resume loaded")

        st.write(
            st.session_state.resume_name
        )

    else:

        st.info("No resume loaded")


with col2:

    if job_available:

        st.success("Job description loaded")

        job_result = st.session_state.job_result

        if job_result:

            st.write(
                job_result.get(
                    "job_title",
                    "Job title not detected"
                )
            )

    else:

        st.info("No job description loaded")


with col3:

    if analysis_available:

        st.success("Analysis completed")

        st.write(
            f"JobFit Score: "
            f"{st.session_state.overall_score}%"
        )

    else:

        st.info("No analysis completed")


# ---------------------------------------------------------
# RESUME INFORMATION
# ---------------------------------------------------------

if resume_available:

    st.divider()

    st.header("Resume Analysis")

    col1, col2 = st.columns(2)


    with col1:

        st.subheader("Resume Skills")

        resume_skills = (
            st.session_state.resume_skills
        )

        if resume_skills:

            st.write(
                ", ".join(
                    skill.title()
                    for skill in resume_skills
                )
            )

        else:

            st.write(
                "No supported skills detected."
            )


    with col2:

        st.subheader("Resume Quality")

        resume_quality = (
            st.session_state.get(
                "resume_quality",
                {}
            )
        )

        quality_score = resume_quality.get(
            "quality_score",
            0
        )

        st.metric(
            "Resume Completeness",
            f"{quality_score}%"
        )


    if resume_quality:

        st.subheader(
            "Resume Sections Detected"
        )

        detected_sections = (
            resume_quality.get(
                "detected_sections",
                []
            )
        )

        if detected_sections:

            st.write(
                ", ".join(
                    section.title()
                    for section in detected_sections
                )
            )

        else:

            st.write(
                "No standard resume sections detected."
            )


# ---------------------------------------------------------
# JOB PARSER RESULTS
# ---------------------------------------------------------

if job_available:

    st.divider()

    st.header("Job Description Analysis")


    job_result = st.session_state.get(
        "job_result"
    )


    if job_result:

        # Job details

        st.subheader("Job Details")

        col1, col2, col3 = st.columns(3)


        with col1:

            st.write("Job Title")

            st.write(
                job_result.get(
                    "job_title",
                    "Not detected"
                )
            )


        with col2:

            st.write("Experience")

            st.write(
                job_result.get(
                    "experience",
                    "Not specified"
                )
            )


        with col3:

            st.write("Education")

            education = job_result.get(
                "education",
                []
            )

            if education:

                st.write(
                    ", ".join(
                        item.title()
                        for item in education
                    )
                )

            else:

                st.write(
                    "Not specified"
                )


        # Required skills

        st.subheader(
            "Required Skills"
        )

        required_skills = job_result.get(
            "required_skills",
            []
        )

        if required_skills:

            st.write(
                ", ".join(
                    skill.title()
                    for skill in required_skills
                )
            )

        else:

            st.write(
                "No required skills detected."
            )


        # Preferred skills

        st.subheader(
            "Preferred Skills"
        )

        preferred_skills = job_result.get(
            "preferred_skills",
            []
        )

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


        # Responsibilities

        st.subheader(
            "Responsibilities"
        )

        responsibilities = job_result.get(
            "responsibilities",
            []
        )

        if responsibilities:

            for responsibility in responsibilities:

                st.write(
                    responsibility
                )

        else:

            st.write(
                "Responsibilities could not be automatically detected."
            )


    else:

        st.info(
            "Job description is loaded, but job analysis "
            "has not been completed yet."
        )


# ---------------------------------------------------------
# MATCHING RESULTS
# ---------------------------------------------------------

if analysis_available:

    st.divider()

    st.header("JobFit Results")


    # Score cards

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "Skill Match",
            f"{st.session_state.skill_score}%"
        )


    with col2:

        st.metric(
            "NLP Similarity",
            f"{st.session_state.text_score}%"
        )


    with col3:

        st.metric(
            "Overall JobFit Score",
            f"{st.session_state.overall_score}%"
        )


    # Skill comparison

    match_result = (
        st.session_state.match_result
    )


    col1, col2 = st.columns(2)


    with col1:

        st.subheader(
            "Matched Skills"
        )

        matched_skills = (
            match_result.get(
                "matched_skills",
                []
            )
        )

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


    with col2:

        st.subheader(
            "Missing Skills"
        )

        missing_skills = (
            match_result.get(
                "missing_skills",
                []
            )
        )

        if missing_skills:

            st.write(
                ", ".join(
                    skill.title()
                    for skill in missing_skills
                )
            )

        else:

            st.write(
                "No missing skills detected."
            )


    # Extra skills

    st.subheader(
        "Additional Resume Skills"
    )

    extra_skills = (
        match_result.get(
            "extra_skills",
            []
        )
    )

    if extra_skills:

        st.write(
            ", ".join(
                skill.title()
                for skill in extra_skills
            )
        )

    else:

        st.write(
            "No additional skills detected."
        )


# ---------------------------------------------------------
# APPLICATION WORKFLOW
# ---------------------------------------------------------

st.divider()

st.header("Application Workflow")

st.write(
    "1. Open Resume Analyzer and upload your resume."
)

st.write(
    "2. Open Job Matcher and paste the target job description."
)

st.write(
    "3. Review the detected job information."
)

st.write(
    "4. Review your JobFit score and skill gaps."
)

st.write(
    "5. Open AI Advisor for personalized recommendations."
)

st.write(
    "6. Open Interview Coach for interview preparation."
)

st.write(
    "7. Use Analysis History to review previous analyses."
)


# ---------------------------------------------------------
# TECHNOLOGY
# ---------------------------------------------------------

st.divider()

st.header("Technology")

st.write(
    "Python | Streamlit | PyMuPDF | Pandas | "
    "Scikit-learn | SQLite | REST API | LLM"
)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "AI JobFit — Resume Analysis, Job Matching, "
    "Skill Gap Analysis and Interview Preparation"
)