from app.data.mock_data import BUSINESS_TYPE_WEIGHTS, NEIGHBORHOOD_SCORES
from app.scoring.engine import calculate_weighted_score
from app.scoring.explanations import generate_explanation


def build_neighborhood_result(
    neighborhood: dict[str, object],
    weights: dict[str, float],
) -> dict[str, object]:
    category_scores = neighborhood["scores"]
    return {
        "id": neighborhood["id"],
        "name": neighborhood["name"],
        "overall_score": calculate_weighted_score(category_scores, weights),
        "category_scores": category_scores,
        "explanation": generate_explanation(category_scores),
    }


def get_recommendations_for_business_type(
    business_type_id: str,
) -> list[dict[str, object]]:
    if business_type_id not in BUSINESS_TYPE_WEIGHTS:
        raise ValueError(f"Unsupported business type: {business_type_id}")

    weights = BUSINESS_TYPE_WEIGHTS[business_type_id]
    recommendations = [
        build_neighborhood_result(neighborhood, weights)
        for neighborhood in NEIGHBORHOOD_SCORES
    ]

    return sorted(
        recommendations,
        key=lambda recommendation: recommendation["overall_score"],
        reverse=True,
    )