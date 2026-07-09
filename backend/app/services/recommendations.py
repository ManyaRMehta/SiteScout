from sqlalchemy.orm import Session

from app.db.models import BusinessType, Neighborhood
from app.scoring.engine import calculate_weighted_score
from app.scoring.explanations import generate_explanation


def _business_type_to_weights(
    business_type: BusinessType,
) -> dict[str, float]:
    return {
        "demand": business_type.demand_weight,
        "competition": business_type.competition_weight,
        "affordability": business_type.affordability_weight,
        "transit": business_type.transit_weight,
        "growth": business_type.growth_weight,
    }


def _neighborhood_to_category_scores(
    neighborhood: Neighborhood,
) -> dict[str, float]:
    return {
        "demand": neighborhood.demand_score,
        "competition": neighborhood.competition_score,
        "affordability": neighborhood.affordability_score,
        "transit": neighborhood.transit_score,
        "growth": neighborhood.growth_score,
    }


def build_neighborhood_result(
    neighborhood: Neighborhood,
    weights: dict[str, float],
) -> dict[str, object]:
    category_scores = _neighborhood_to_category_scores(neighborhood)

    return {
        "id": neighborhood.id,
        "name": neighborhood.name,
        "overall_score": calculate_weighted_score(category_scores, weights),
        "category_scores": category_scores,
        "explanation": generate_explanation(category_scores),
    }


def get_recommendations_for_business_type(
    db: Session,
    business_type_id: str,
) -> list[dict[str, object]]:
    business_type = db.get(BusinessType, business_type_id)

    if business_type is None:
        raise ValueError(f"Unsupported business type: {business_type_id}")

    weights = _business_type_to_weights(business_type)
    neighborhoods = db.query(Neighborhood).all()

    recommendations = [
        build_neighborhood_result(neighborhood, weights)
        for neighborhood in neighborhoods
    ]

    return sorted(
        recommendations,
        key=lambda recommendation: recommendation["overall_score"],
        reverse=True,
    )