from app.data.mock_data import BUSINESS_TYPE_WEIGHTS, NEIGHBORHOOD_SCORES
from app.scoring.engine import calculate_weighted_score


def get_recommendations_for_business_type(
    business_type_id: str,
) -> list[dict[str, object]]:
    if business_type_id not in BUSINESS_TYPE_WEIGHTS:
        raise ValueError(f"Unsupported business type: {business_type_id}")

    weights = BUSINESS_TYPE_WEIGHTS[business_type_id]
    recommendations = []

    for neighborhood in NEIGHBORHOOD_SCORES:
        category_scores = neighborhood["scores"]
        overall_score = calculate_weighted_score(category_scores, weights)

        recommendation = {
            "id": neighborhood["id"],
            "name": neighborhood["name"],
            "overall_score": overall_score,
            "category_scores": category_scores,
        }

        recommendations.append(recommendation)

    return sorted(
        recommendations,
        key=lambda recommendation: recommendation["overall_score"],
        reverse=True,
    )