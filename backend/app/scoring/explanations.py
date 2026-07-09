STRENGTH_LABELS = {
    "demand": "strong customer demand",
    "transit": "good transit and accessibility",
    "affordability": "affordability",
    "growth": "growth potential",
}


def generate_explanation(category_scores: dict[str, float]) -> str:
    strengths = [
        label
        for category, label in STRENGTH_LABELS.items()
        if category_scores[category] >= 75
    ]

    if category_scores["competition"] >= 50:
        competition_sentence = "Competition appears manageable."
    else:
        competition_sentence = (
            "High competition may mean differentiation is important."
        )

    if not strengths:
        return competition_sentence

    if len(strengths) == 1:
        strength_phrase = strengths[0]
    elif len(strengths) == 2:
        strength_phrase = f"{strengths[0]} and {strengths[1]}"
    else:
        strength_phrase = ", ".join(strengths[:-1]) + f", and {strengths[-1]}"

    return f"This neighborhood offers {strength_phrase}. {competition_sentence}"
