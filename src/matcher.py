
# ============================================================
# SKILL CATEGORIES
# ============================================================

SKILL_WEIGHTS = {

    # Core programming
    "python": 3,
    "java": 3,
    "c++": 3,

    # Databases
    "sql": 3,
    "mysql": 2,
    "postgresql": 2,
    "sqlite": 1,

    # Data and ML
    "pandas": 2,
    "numpy": 2,
    "scikit-learn": 2,
    "pytorch": 2,
    "pytorch geometric": 2,

    "machine learning": 3,
    "deep learning": 3,
    "natural language processing": 3,

    "data preprocessing": 2,
    "feature engineering": 2,
    "classification": 2,
    "regression": 2,
    "model training": 2,
    "model evaluation": 2,

    # Data visualization
    "power bi": 2,
    "tableau": 2,
    "excel": 1,

    # Web development
    "html": 1,
    "css": 1,
    "javascript": 2,
    "react": 2,

    "django": 3,
    "flask": 3,
    "fastapi": 3,
    "streamlit": 2,

    "rest api": 2,

    # DevOps / Cloud
    "git": 1,
    "github": 1,
    "docker": 2,
    "aws": 2,
    "azure": 2,
    "linux": 2,

    # Enterprise platforms
    "salesforce": 3,
    "servicenow": 3,

    # Programming concepts
    "oop": 2,
    "object-oriented programming": 2,
    "data structures": 2,
    "functions": 1,
    "modules": 1,
    "file handling": 1,
    "exception handling": 1,
    "collections": 1,
    "crud operations": 1,
}


# ============================================================
# GET SKILL WEIGHT
# ============================================================

def get_skill_weight(skill):
    """
    Return the importance weight of a skill.

    Skills not present in the weight dictionary
    receive a default weight of 1.
    """

    return SKILL_WEIGHTS.get(
        skill,
        1
    )


# ============================================================
# CALCULATE WEIGHTED MATCH
# ============================================================

def calculate_match(
    resume_skills,
    job_skills
):
    """
    Compare resume skills with job-required skills.

    The score is weighted according to the importance
    assigned to each detected job skill.
    """

    resume_set = set(
        resume_skills
    )

    job_set = set(
        job_skills
    )


    # --------------------------------------------------------
    # Matched skills
    # --------------------------------------------------------

    matched_skills = (
        resume_set.intersection(
            job_set
        )
    )


    # --------------------------------------------------------
    # Missing skills
    # --------------------------------------------------------

    missing_skills = (
        job_set.difference(
            resume_set
        )
    )


    # --------------------------------------------------------
    # Extra resume skills
    # --------------------------------------------------------

    extra_skills = (
        resume_set.difference(
            job_set
        )
    )


    # --------------------------------------------------------
    # Calculate total possible weight
    # --------------------------------------------------------

    total_weight = sum(
        get_skill_weight(skill)
        for skill in job_set
    )


    # --------------------------------------------------------
    # Calculate matched weight
    # --------------------------------------------------------

    matched_weight = sum(
        get_skill_weight(skill)
        for skill in matched_skills
    )


    # --------------------------------------------------------
    # Calculate score
    # --------------------------------------------------------

    if total_weight == 0:

        match_score = 0

    else:

        match_score = (
            matched_weight
            / total_weight
        ) * 100


    # --------------------------------------------------------
    # Return results
    # --------------------------------------------------------

    return {

        "matched_skills": sorted(
            matched_skills
        ),

        "missing_skills": sorted(
            missing_skills
        ),

        "extra_skills": sorted(
            extra_skills
        ),

        "match_score": round(
            match_score,
            2
        ),

        "matched_weight": matched_weight,

        "total_weight": total_weight
    }

