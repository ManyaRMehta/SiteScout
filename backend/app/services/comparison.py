from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.db.models import BusinessType, Neighborhood
from app.services.recommendations import (
    _business_type_to_weights,
    build_neighborhood_result,
)


def _find_neighborhood(
    db: Session,
    neighborhood_identifier: str,
) -> Neighborhood:
    normalized_identifier = neighborhood_identifier.strip().lower()

    neighborhood = (
        db.query(Neighborhood)
        .filter(
            or_(
                Neighborhood.id == normalized_identifier,
                Neighborhood.name.ilike(neighborhood_identifier.strip()),
            )
        )
        .first()
    )

    if neighborhood is None:
        raise ValueError(f"Unsupported neighborhood: {neighborhood_identifier}")

    return neighborhood


def compare_neighborhoods(
    db: Session,
    business_type_id: str,
    neighborhood_a: str,
    neighborhood_b: str,
) -> dict[str, object]:
    business_type = db.get(BusinessType, business_type_id)

    if business_type is None:
        raise ValueError(f"Unsupported business type: {business_type_id}")

    weights = _business_type_to_weights(business_type)

    result_a = build_neighborhood_result(
        _find_neighborhood(db, neighborhood_a),
        weights,
    )
    result_b = build_neighborhood_result(
        _find_neighborhood(db, neighborhood_b),
        weights,
    )

    score_a = result_a["overall_score"]
    score_b = result_b["overall_score"]

    readable_business_type = business_type_id.replace("_", " ")

    if score_a > score_b:
        winner = result_a["name"]
        summary = (
            f"{result_a['name']} scores higher overall ({score_a} vs {score_b}) "
            f"for {readable_business_type}."
        )
    elif score_b > score_a:
        winner = result_b["name"]
        summary = (
            f"{result_b['name']} scores higher overall ({score_b} vs {score_a}) "
            f"for {readable_business_type}."
        )
    else:
        winner = "tie"
        summary = (
            f"{result_a['name']} and {result_b['name']} are tied "
            f"with a score of {score_a}."
        )

    return {
        "business_type": business_type_id,
        "neighborhood_a": result_a,
        "neighborhood_b": result_b,
        "winner": winner,
        "summary": summary,
    }