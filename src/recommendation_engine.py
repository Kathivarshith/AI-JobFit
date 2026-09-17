RECOMMENDATIONS = {

    "python": {
        "learn": "Advanced Python, OOP, Decorators",
        "project": "Build a REST API",
        "interview": "Functions, OOP, Exception Handling"
    },

    "sql": {
        "learn": "Joins, Window Functions",
        "project": "Employee Database System",
        "interview": "Joins, Indexes, Normalization"
    },

    "mysql": {
        "learn": "Database Design",
        "project": "Library Management System",
        "interview": "Primary Keys, Foreign Keys"
    },

    "docker": {
        "learn": "Docker Containers",
        "project": "Containerize a Flask App",
        "interview": "Images, Containers, Volumes"
    },

    "fastapi": {
        "learn": "FastAPI Framework",
        "project": "Job Portal API",
        "interview": "REST APIs, CRUD Operations"
    },

    "django": {
        "learn": "Django Framework",
        "project": "Blog Website",
        "interview": "Models, Views, Templates"
    },

    "git": {
        "learn": "Git Branching",
        "project": "Collaborative Project",
        "interview": "Merge, Rebase, Pull Requests"
    }
}


def generate_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:

        if skill in RECOMMENDATIONS:

            recommendations.append({

                "skill": skill,

                "learn": RECOMMENDATIONS[skill]["learn"],

                "project": RECOMMENDATIONS[skill]["project"],

                "interview": RECOMMENDATIONS[skill]["interview"]

            })

    return recommendations


# ============================================================
# RESUME RECOMMENDATIONS
# ============================================================

SECTION_RECOMMENDATIONS = {

    "summary": (
        "Add a short professional summary describing "
        "your technical background, key skills, and the "
        "type of role you are targeting."
    ),

    "skills": (
        "Add a clearly organized technical skills section "
        "containing the programming languages, frameworks, "
        "databases, tools, and technologies you actually know."
    ),

    "education": (
        "Add your education details including degree, "
        "institution, graduation year, and relevant academic "
        "information."
    ),

    "experience": (
        "Add relevant internship, work, or practical experience. "
        "Describe your responsibilities and measurable results "
        "where applicable."
    ),

    "projects": (
        "Add 2 to 4 relevant projects. Include the technologies "
        "used, what you built, and your specific contribution."
    ),

    "certifications": (
        "Add relevant certifications that support the job "
        "you are applying for."
    )
}


# ============================================================
# GENERATE RECOMMENDATIONS
# ============================================================

def generate_resume_recommendations(
    missing_sections,
    contact_information
):
    """
    Generate resume improvement recommendations
    based on missing sections and contact information.
    """

    recommendations = []


    # --------------------------------------------------------
    # Missing section recommendations
    # --------------------------------------------------------

    for section in missing_sections:

        if section in SECTION_RECOMMENDATIONS:

            recommendations.append(
                SECTION_RECOMMENDATIONS[section]
            )


    # --------------------------------------------------------
    # Contact information recommendations
    # --------------------------------------------------------

    if not contact_information.get(
        "email",
        False
    ):

        recommendations.append(
            "Add a professional email address to the "
            "resume header."
        )


    if not contact_information.get(
        "phone",
        False
    ):

        recommendations.append(
            "Add a valid phone number to the resume header."
        )


    if not contact_information.get(
        "linkedin",
        False
    ):

        recommendations.append(
            "Add your LinkedIn profile URL to make your "
            "professional profile easier to find."
        )


    if not contact_information.get(
        "github",
        False
    ):

        recommendations.append(
            "Consider adding your GitHub profile if you "
            "have relevant public projects."
        )


    # --------------------------------------------------------
    # Default recommendation
    # --------------------------------------------------------

    if not recommendations:

        recommendations.append(
            "The resume contains the commonly expected "
            "sections detected by this analyzer. Focus on "
            "improving the relevance and clarity of your "
            "projects and experience for each target job."
        )


    return recommendations

