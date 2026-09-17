import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def build_ai_prompt(
    resume_text,
    job_description,
    matched_skills,
    missing_skills,
    overall_score
):
    prompt = f"""
You are an AI career advisor.

Analyze the candidate's resume against the job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

MATCHED SKILLS:
{", ".join(matched_skills)}

MISSING SKILLS:
{", ".join(missing_skills)}

OVERALL JOBFIT SCORE:
{overall_score}%

Provide:

1. Resume-job alignment analysis
2. Most important skill gaps
3. Specific recommendations to improve the resume
4. Recommended projects
5. Interview preparation topics
6. Three suggested improvements to resume bullet points

Be practical and concise.
Do not invent experience that is not present in the resume.
"""

    return prompt


def get_ai_advice(
    resume_text,
    job_description,
    matched_skills,
    missing_skills,
    overall_score
):

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY was not found."
        )

    client = OpenAI(
        api_key=api_key
    )

    prompt = build_ai_prompt(
        resume_text,
        job_description,
        matched_skills,
        missing_skills,
        overall_score
    )

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text


def get_interview_questions(
    resume_text,
    job_description,
    matched_skills,
    missing_skills,
    overall_score
):

    from src.interview_coach import build_interview_prompt

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY was not found."
        )

    client = OpenAI(
        api_key=api_key
    )

    prompt = build_interview_prompt(
        resume_text,
        job_description,
        matched_skills,
        missing_skills,
        overall_score
    )

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt
    )

    return response.output_text