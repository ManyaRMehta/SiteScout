from app.data.mock_data import BUSINESS_TYPE_WEIGHTS, NEIGHBORHOOD_SCORES
from app.services.recommendations import build_neighborhood_result


def _find_neighborhood(name: str) -> dict[str, object]:
    normalized_name = name.strip().lower()
    for neighborhood in NEIGHBORHOOD_SCORES:
        if neighborhood["name"].lower() == normalized_name:
            return neighborhood
    raise ValueError(f"Unsupported neighborhood: {name}")


def compare_neighborhoods(
    business_type: str,
    neighborhood_a: str,
    neighborhood_b: str,
) -> dict[str, object]:
    if business_type not in BUSINESS_TYPE_WEIGHTS:
        raise ValueError(f"Unsupported business type: {business_type}")

    weights = BUSINESS_TYPE_WEIGHTS[business_type]
    result_a = build_neighborhood_result(_find_neighborhood(neighborhood_a), weights)
    result_b = build_neighborhood_result(_find_neighborhood(neighborhood_b), weights)

    score_a = result_a["overall_score"]
    score_b = result_b["overall_score"]

    if score_a > score_b:
        winner = result_a["name"]
        summary = (
            f"{result_a['name']} scores higher overall ({score_a} vs {score_b}) "
            f"for {business_type.replace('_', ' ')}."
        )
    elif score_b > score_a:
        winner = result_b["name"]
        summary = (
            f"{result_b['name']} scores higher overall ({score_b} vs {score_a}) "
            f"for {business_type.replace('_', ' ')}."
        )
    else:
        winner = "tie"
        summary = (
            f"{result_a['name']} and {result_b['name']} are tied "
            f"with a score of {score_a}."
        )

    return {
        "business_type": business_type,
        "neighborhood_a": result_a,
        "neighborhood_b": result_b,
        "winner": winner,
        "summary": summary,
    }
