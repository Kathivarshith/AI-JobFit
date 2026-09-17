def generate_resume_recommendations(
    missing_sections,
    contact_information
):
    recommendations = []

    # Resume sections
    section_recommendations = {
        "summary": (
            "Add a concise professional summary describing "
            "your background, key skills and target role."
        ),

        "skills": (
            "Add a dedicated Skills section containing "
            "technical skills relevant to the target job."
        ),

        "education": (
            "Add your Education section with degree, "
            "institution, graduation year and relevant academic details."
        ),

        "experience": (
            "Add an Experience section describing internships, "
            "training or relevant professional experience."
        ),

        "projects": (
            "Add relevant projects with technologies used, "
            "your contribution and measurable results."
        ),

        "certifications": (
            "Add relevant certifications that support "
            "the requirements of your target role."
        ),

        "contact": (
            "Make sure your contact information is clearly "
            "visible at the top of your resume."
        )
    }

    for section in missing_sections:

        section_lower = section.lower()

        if section_lower in section_recommendations:

            recommendations.append(
                section_recommendations[section_lower]
            )

    # Contact information
    if not contact_information.get("email", False):

        recommendations.append(
            "Add a professional email address to your resume."
        )

    if not contact_information.get("phone", False):

        recommendations.append(
            "Add a valid phone number so recruiters can contact you."
        )

    if not contact_information.get("linkedin", False):

        recommendations.append(
            "Add your LinkedIn profile URL to improve your professional visibility."
        )

    if not contact_information.get("github", False):

        recommendations.append(
            "Add your GitHub profile if you have relevant technical projects."
        )

    # Default recommendation
    if not recommendations:

        recommendations.append(
            "Your resume structure looks complete. "
            "Focus on tailoring keywords and project descriptions "
            "to each target job."
        )

    return recommendations