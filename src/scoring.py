
# ============================================================
# SCORE CONFIGURATION
# ============================================================

SKILL_WEIGHT = 0.70
TEXT_WEIGHT = 0.30


# ============================================================
# CALCULATE OVERALL SCORE
# ============================================================

def calculate_overall_score(
    skill_score,
    text_score
):
    """
    Calculate the overall JobFit score.

    The current project design uses:
    70% skill matching
    30% textual similarity
    """

    overall_score = (
        skill_score * SKILL_WEIGHT
        + text_score * TEXT_WEIGHT
    )

    return round(
        overall_score,
        2
    )


# ============================================================
# GET SCORE BREAKDOWN
# ============================================================

def get_score_breakdown(
    skill_score,
    text_score
):
    """
    Return a detailed explanation of how
    the overall JobFit score was calculated.
    """

    skill_contribution = (
        skill_score * SKILL_WEIGHT
    )

    text_contribution = (
        text_score * TEXT_WEIGHT
    )

    overall_score = (
        skill_contribution
        + text_contribution
    )

    return {
        "skill_score": round(
            skill_score,
            2
        ),

        "text_score": round(
            text_score,
            2
        ),

        "skill_weight": SKILL_WEIGHT,

        "text_weight": TEXT_WEIGHT,

        "skill_contribution": round(
            skill_contribution,
            2
        ),

        "text_contribution": round(
            text_contribution,
            2
        ),

        "overall_score": round(
            overall_score,
            2
        )
    }

