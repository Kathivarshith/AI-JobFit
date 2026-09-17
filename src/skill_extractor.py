
import re

# CANONICAL SKILLS

SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "mysql",
    "postgresql",
    "sqlite",

    "pandas",
    "numpy",
    "scikit-learn",
    "pytorch",
    "pytorch geometric",

    "machine learning",
    "deep learning",
    "natural language processing",
    "data preprocessing",
    "feature engineering",
    "classification",
    "regression",
    "model training",
    "model evaluation",

    "power bi",
    "tableau",
    "excel",

    "html",
    "css",
    "javascript",
    "react",

    "django",
    "flask",
    "fastapi",
    "streamlit",

    "rest api",

    "git",
    "github",
    "docker",
    "aws",
    "azure",
    "linux",

    "salesforce",
    "servicenow",

    "oop",
    "object-oriented programming",
    "data structures",
    "functions",
    "modules",
    "file handling",
    "exception handling",
    "collections",
    "crud operations",
]



# SKILL ALIASES


SKILL_ALIASES = {

    "ml": "machine learning",

    "machine-learning": "machine learning",

    "ai": "artificial intelligence",

    "nlp": "natural language processing",

    "natural-language-processing":
        "natural language processing",

    "rest api": "rest api",

    "rest apis": "rest api",

    "restful api": "rest api",

    "restful apis": "rest api",

    "react.js": "react",

    "reactjs": "react",

    "node.js": "node.js",

    "nodejs": "node.js",

    "scikit learn": "scikit-learn",

    "sklearn": "scikit-learn",

    "pytorch-geometric":
        "pytorch geometric",

    "object oriented programming":
        "object-oriented programming",

    "object-oriented":
        "object-oriented programming",

    "mysql database":
        "mysql",

    "my sql":
        "mysql",

    "powerbi":
        "power bi",

    "git hub":
        "github",

    "service now":
        "servicenow",
}


# ============================================================
# NORMALIZE TEXT
# ============================================================

def normalize_text(text):
    """
    Normalize text before skill extraction.
    """

    text = text.lower()

    # Replace common punctuation variations
    text = text.replace("–", "-")
    text = text.replace("—", "-")

    # Remove extra whitespace
    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()


# ============================================================
# CHECK SKILL IN TEXT
# ============================================================

def skill_exists(
    skill,
    text
):
    """
    Check whether a skill exists in the text.
    """

    # Special handling for skills containing
    # characters that are not word characters.

    if skill in [
        "c++",
        "scikit-learn",
        "object-oriented programming"
    ]:

        return skill in text


    pattern = (
        r"(?<!\w)"
        + re.escape(skill)
        + r"(?!\w)"
    )

    return bool(
        re.search(
            pattern,
            text
        )
    )


# ============================================================
# EXTRACT SKILLS
# ============================================================

def extract_skills(text):
    """
    Extract and normalize technical skills
    from resume or job-description text.
    """

    text = normalize_text(text)

    found_skills = set()


    # --------------------------------------------------------
    # Check aliases first
    # --------------------------------------------------------

    for alias, canonical_skill in SKILL_ALIASES.items():

        if skill_exists(
            alias,
            text
        ):

            found_skills.add(
                canonical_skill
            )


    # --------------------------------------------------------
    # Check canonical skills
    # --------------------------------------------------------

    for skill in SKILLS:

        if skill_exists(
            skill,
            text
        ):

            found_skills.add(
                skill
            )


    # --------------------------------------------------------
    # Remove generic REST/API duplication
    # --------------------------------------------------------

    # REST API already represents API knowledge
    # for our matching system.

    if "rest api" in found_skills:

        found_skills.discard(
            "api"
        )


    return sorted(
        found_skills
    )

