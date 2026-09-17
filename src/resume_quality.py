
import re


# ============================================================
# RESUME SECTIONS
# ============================================================

RESUME_SECTIONS = {

    "summary": [
        "summary",
        "professional summary",
        "career objective",
        "objective",
        "profile"
    ],

    "skills": [
        "skills",
        "technical skills",
        "technical skill",
        "key skills"
    ],

    "education": [
        "education",
        "academic background",
        "educational qualifications"
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment"
    ],

    "projects": [
        "projects",
        "academic projects",
        "personal projects",
        "project"
    ],

    "certifications": [
        "certifications",
        "certificates",
        "licenses and certifications"
    ],

    "contact": [
        "email",
        "phone",
        "linkedin",
        "github"
    ]
}


# ============================================================
# SECTION DETECTION
# ============================================================

def detect_resume_sections(text):
    """
    Detect common resume sections.
    """

    text = text.lower()

    detected_sections = []

    for section, keywords in RESUME_SECTIONS.items():

        for keyword in keywords:

            if re.search(
                r"(?<!\w)"
                + re.escape(keyword)
                + r"(?!\w)",
                text
            ):

                detected_sections.append(
                    section
                )

                break

    return sorted(
        detected_sections
    )


# ============================================================
# MISSING SECTIONS
# ============================================================

def find_missing_sections(detected_sections):
    """
    Identify commonly expected resume sections
    that were not detected.
    """

    important_sections = [
        "summary",
        "skills",
        "education",
        "experience",
        "projects",
        "certifications"
    ]

    missing_sections = []

    for section in important_sections:

        if section not in detected_sections:

            missing_sections.append(
                section
            )

    return missing_sections


# ============================================================
# CONTACT INFORMATION
# ============================================================

def analyze_contact_information(text):
    """
    Check for common contact information.
    """

    email_found = bool(
        re.search(
            r"[A-Za-z0-9._%+-]+"
            r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text
        )
    )

    phone_found = bool(
        re.search(
            r"(?:\+91[\s-]?)?"
            r"[6-9]\d{9}",
            text
        )
    )

    linkedin_found = (
        "linkedin.com" in text.lower()
    )

    github_found = (
        "github.com" in text.lower()
    )

    return {
        "email": email_found,
        "phone": phone_found,
        "linkedin": linkedin_found,
        "github": github_found
    }


# ============================================================
# RESUME QUALITY SCORE
# ============================================================

def calculate_resume_quality_score(
    detected_sections,
    contact_information
):
    """
    Calculate a simple resume completeness score.

    This is a project-defined completeness score,
    not an ATS prediction.
    """

    important_sections = [
        "summary",
        "skills",
        "education",
        "experience",
        "projects",
        "certifications"
    ]

    section_points = 0

    for section in important_sections:

        if section in detected_sections:

            section_points += 10


    contact_points = 0

    for field in contact_information.values():

        if field:

            contact_points += 5


    score = (
        section_points
        + contact_points
    )

    return min(
        score,
        100
    )


# ============================================================
# COMPLETE RESUME ANALYSIS
# ============================================================

def analyze_resume_quality(text):
    """
    Perform complete resume quality analysis.
    """

    detected_sections = detect_resume_sections(
        text
    )

    missing_sections = find_missing_sections(
        detected_sections
    )

    contact_information = analyze_contact_information(
        text
    )

    quality_score = calculate_resume_quality_score(
        detected_sections,
        contact_information
    )

    return {
        "detected_sections": detected_sections,
        "missing_sections": missing_sections,
        "contact_information": contact_information,
        "quality_score": quality_score
    }

