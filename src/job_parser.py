import re

from src.skill_extractor import extract_skills


def extract_job_title(job_description):
    lines = [
        line.strip()
        for line in job_description.splitlines()
        if line.strip()
    ]

    title_keywords = [
        "python developer",
        "software developer",
        "software engineer",
        "data analyst",
        "data scientist",
        "machine learning engineer",
        "frontend developer",
        "backend developer",
        "full stack developer",
        "salesforce administrator",
        "salesforce admin",
        "system administrator",
        "network engineer",
        "cloud engineer",
        "devops engineer",
        "business analyst",
        "technical support engineer",
        "technical support",
        "support engineer"
    ]

    text = job_description.lower()

    for title in title_keywords:

        if title in text:
            return title.title()

    # Check the first few lines as a fallback
    for line in lines[:5]:

        if len(line) <= 100:
            return line

    return "Not detected"


def extract_experience_requirement(job_description):

    patterns = [
        r"\b\d+\s*(?:-|to)\s*\d+\s+years?\b",
        r"\b\d+\+?\s+years?\b",
        r"\b\d+\s*(?:-|to)\s*\d+\s+yrs?\b",
        r"\b\d+\+?\s+yrs?\b"
    ]

    text = job_description.lower()

    for pattern in patterns:

        match = re.search(
            pattern,
            text
        )

        if match:
            return match.group(0)

    return "Not specified"


def extract_education_requirement(job_description):

    education_keywords = [
        "bachelor's degree",
        "bachelor degree",
        "b.tech",
        "b.e",
        "b.sc",
        "bca",
        "master's degree",
        "master degree",
        "m.tech",
        "m.e",
        "m.sc",
        "mca",
        "degree in computer science",
        "degree in engineering",
        "computer science degree"
    ]

    text = job_description.lower()

    detected = []

    for keyword in education_keywords:

        if keyword in text:
            detected.append(keyword)

    return sorted(
        set(detected)
    )


def extract_responsibilities(job_description):

    lines = [
        line.strip()
        for line in job_description.splitlines()
        if line.strip()
    ]

    responsibility_headings = [
        "responsibilities",
        "responsibility",
        "what you will do",
        "what you'll do",
        "job responsibilities",
        "job duties",
        "duties",
        "role and responsibilities"
    ]

    stop_headings = [
        "requirements",
        "required skills",
        "qualifications",
        "preferred",
        "preferred skills",
        "nice to have",
        "nice-to-have",
        "education",
        "benefits",
        "about us"
    ]

    responsibilities = []

    capture = False

    for line in lines:

        lower_line = line.lower().strip()

        # Start capturing after a responsibility heading
        if any(
            heading == lower_line
            or lower_line.startswith(
                heading + ":"
            )
            for heading in responsibility_headings
        ):
            capture = True
            continue

        # Stop when another major section starts
        if capture and any(
            lower_line == heading
            or lower_line.startswith(
                heading + ":"
            )
            for heading in stop_headings
        ):
            capture = False
            continue

        if capture:

            cleaned_line = line.strip(
                "-•* "
            )

            if cleaned_line:
                responsibilities.append(
                    cleaned_line
                )

    return responsibilities[:10]


def extract_preferred_skills(job_description):

    lines = [
        line.strip()
        for line in job_description.splitlines()
        if line.strip()
    ]

    preferred_headings = [
        "preferred",
        "preferred skills",
        "preferred qualifications",
        "nice to have",
        "nice-to-have",
        "good to have",
        "bonus",
        "additional skills"
    ]

    stop_headings = [
        "requirements",
        "required skills",
        "qualifications",
        "responsibilities",
        "responsibility",
        "what you will do",
        "education",
        "benefits",
        "about us"
    ]

    preferred_text = []

    capture = False

    for line in lines:

        lower_line = line.lower().strip()

        # Start preferred section
        if any(
            heading == lower_line
            or lower_line.startswith(
                heading + ":"
            )
            for heading in preferred_headings
        ):
            capture = True
            continue

        # Stop preferred section
        if capture and any(
            heading == lower_line
            or lower_line.startswith(
                heading + ":"
            )
            for heading in stop_headings
        ):
            capture = False
            continue

        if capture:

            cleaned_line = line.strip(
                "-•* "
            )

            if cleaned_line:
                preferred_text.append(
                    cleaned_line
                )

    return extract_skills(
        " ".join(preferred_text)
    )


def analyze_job_description(job_description):

    if not job_description:
        return {
            "job_title": "Not detected",
            "skills": [],
            "required_skills": [],
            "preferred_skills": [],
            "experience": "Not specified",
            "education": [],
            "responsibilities": []
        }

    all_skills = extract_skills(
        job_description
    )

    preferred_skills = extract_preferred_skills(
        job_description
    )

    required_skills = [
        skill
        for skill in all_skills
        if skill not in preferred_skills
    ]

    return {
        "job_title": extract_job_title(
            job_description
        ),

        "skills": sorted(
            required_skills
        ),

        "required_skills": sorted(
            required_skills
        ),

        "preferred_skills": sorted(
            preferred_skills
        ),

        "experience": extract_experience_requirement(
            job_description
        ),

        "education": extract_education_requirement(
            job_description
        ),

        "responsibilities": extract_responsibilities(
            job_description
        )
    }