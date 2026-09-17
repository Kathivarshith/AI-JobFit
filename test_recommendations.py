from src.recommendation_engine import generate_recommendations


missing_skills = [
    "fastapi",
    "docker"
]


result = generate_recommendations(
    missing_skills
)


for item in result:

    print(item)