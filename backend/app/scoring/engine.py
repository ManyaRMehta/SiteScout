DEFAULT_WEIGHTS = {
    "demand": 0.20,
    "competition": 0.20,
    "affordability": 0.20,
    "transit": 0.20,
    "growth": 0.20,
}

REQUIRED_CATEGORIES = set(DEFAULT_WEIGHTS.keys())


def calculate_weighted_score(
    category_scores: dict[str, float],
    weights: dict[str, float] = DEFAULT_WEIGHTS,
) -> float:
    missing_score_categories = REQUIRED_CATEGORIES - set(category_scores.keys())
    if missing_score_categories:
        raise ValueError(f"Missing category scores: {missing_score_categories}")

    missing_weight_categories = REQUIRED_CATEGORIES - set(weights.keys())
    if missing_weight_categories:
        raise ValueError(f"Missing weight categories: {missing_weight_categories}")

    for category, score in category_scores.items():
        if category not in REQUIRED_CATEGORIES:
            raise ValueError(f"Unknown score category: {category}")

        if score < 0 or score > 100:
            raise ValueError(f"Score for {category} must be between 0 and 100")

    total_score = 0.0

    for category in REQUIRED_CATEGORIES:
        total_score += category_scores[category] * weights[category]

    return round(total_score, 2)