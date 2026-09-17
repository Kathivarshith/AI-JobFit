def build_interview_prompt(
    resume_text,
    job_description,
    matched_skills,
    missing_skills,
    overall_score
):
    prompt = f"""
You are an interview preparation coach.

Prepare the candidate for the target job using only
the information available in the resume and job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

MATCHED SKILLS:
{", ".join(matched_skills)}

MISSING SKILLS:
{", ".join(missing_skills)}

JOBFIT SCORE:
{overall_score}%

Generate an interview preparation guide containing:

1. Technical Interview Questions

Generate 5 technical questions based on the
technologies and skills mentioned in the job description.

For every question provide:

Question:
What the interviewer expects:
Short sample answer:

2. Resume and Project Questions

Generate 3 questions based specifically on
the projects, internship, education, and skills
actually present in the resume.

For every question provide:

Question:
What the interviewer expects:
Short sample answer:

3. HR Questions

Generate 3 common HR questions suitable for a fresher.

For every question provide:

Question:
What the interviewer expects:
Short sample answer:

4. Skill Gap Questions

Generate 3 questions related to the missing skills.

For every question provide:

Question:
What the interviewer expects:
Short sample answer:

The candidate is a fresher.

Keep answers:

- Short
- Easy to understand
- Easy to speak in an interview
- Technically accurate
- Based only on the candidate's actual background

Do not invent projects, internships, certifications,
skills, work experience, or achievements.

5. Preparation Plan

Provide a short preparation plan with:

Day 1:
Day 2:
Day 3:
Day 4:
Day 5:

Focus the preparation on the most relevant job requirements
and identified skill gaps.
"""

    return prompt