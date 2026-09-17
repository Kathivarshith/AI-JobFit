def generate_resume_advice(
    missing_skills,
    matched_skills,
    overall_score
):
    """
    Generate resume improvement suggestions
    based on the job match analysis.
    """

    advice = []

    # Score-based advice
    if overall_score < 50:

        advice.append(
            "Your resume has a relatively low match with this job. "
            "Consider adding relevant projects and skills from the job description."
        )

    elif overall_score < 75:

        advice.append(
            "Your resume has a moderate match. "
            "Focus on the missing technical skills and strengthen relevant project descriptions."
        )

    else:

        advice.append(
            "Your resume has strong alignment with the detected job requirements. "
            "Focus on clearly demonstrating your experience with the matched skills."
        )


    # Missing skill advice
    if missing_skills:

        skills = ", ".join(
            skill.title()
            for skill in missing_skills
        )

        advice.append(
            f"Consider learning or gaining project experience with: {skills}."
        )


    # Matched skill advice
    if matched_skills:

        advice.append(
            "Make sure your resume provides evidence for your matched skills "
            "through projects, internships, certifications, or measurable achievements."
        )


    return advice