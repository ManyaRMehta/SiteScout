from app.data.mock_data import BUSINESS_TYPE_WEIGHTS, NEIGHBORHOOD_SCORES
from app.scoring.engine import REQUIRED_CATEGORIES
from app.services.recommendations import (
    build_neighborhood_result,
    get_recommendations_for_business_type,
)


def _validate_custom_weights(custom_weights: dict[str, float]) -> None:
    received_categories = set(custom_weights.keys())

    missing_categories = REQUIRED_CATEGORIES - received_categories
    if missing_categories:
        raise ValueError(f"Missing custom weight categories: {missing_categories}")

    extra_categories = received_categories - REQUIRED_CATEGORIES
    if extra_categories:
        raise ValueError(f"Unknown custom weight categories: {extra_categories}")

    for category, weight in custom_weights.items():
        if weight < 0 or weight > 1:
            raise ValueError(f"Weight for {category} must be between 0 and 1")

    total_weight = sum(custom_weights.values())
    if total_weight < 0.99 or total_weight > 1.01:
        raise ValueError(
            f"Custom weights must sum to 1.0. Current total: {round(total_weight, 2)}"
        )


def _get_highest_weight_category(custom_weights: dict[str, float]) -> str:
    return max(custom_weights, key=custom_weights.get)


def get_what_if_recommendations(
    business_type_id: str,
    custom_weights: dict[str, float],
) -> dict[str, object]:
    if business_type_id not in BUSINESS_TYPE_WEIGHTS:
        raise ValueError(f"Unsupported business type: {business_type_id}")

    _validate_custom_weights(custom_weights)

    default_recommendations = get_recommendations_for_business_type(business_type_id)
    previous_rank_by_id = {
        recommendation["id"]: rank
        for rank, recommendation in enumerate(default_recommendations, start=1)
    }

    custom_recommendations = [
        build_neighborhood_result(neighborhood, custom_weights)
        for neighborhood in NEIGHBORHOOD_SCORES
    ]

    ranked_custom_recommendations = sorted(
        custom_recommendations,
        key=lambda recommendation: recommendation["overall_score"],
        reverse=True,
    )

    recommendations_with_rank_changes = []

    for new_rank, recommendation in enumerate(ranked_custom_recommendations, start=1):
        previous_rank = previous_rank_by_id[recommendation["id"]]

        recommendations_with_rank_changes.append(
            {
                **recommendation,
                "previous_rank": previous_rank,
                "new_rank": new_rank,
                "rank_change": previous_rank - new_rank,
            }
        )

    highest_weight_category = _get_highest_weight_category(custom_weights)
    readable_business_type = business_type_id.replace("_", " ")
    readable_category = highest_weight_category.replace("_", " ")

    summary = (
        f"These what-if results rank neighborhoods for a {readable_business_type} "
        f"using your custom priorities. The highest-weighted factor is "
        f"{readable_category}, so neighborhoods strong in that category may move up."
    )

    return {
        "business_type_id": business_type_id,
        "custom_weights": custom_weights,
        "recommendations": recommendations_with_rank_changes,
        "summary": summary,
    }