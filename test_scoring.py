from src.scoring import calculate_overall_score


skill_score = 80
text_score = 60

overall = calculate_overall_score(
    skill_score,
    text_score
)

print("Overall JobFit Score:", overall, "%")
