from fastapi import APIRouter, HTTPException

from app.schemas.recommendations import (
    CompareRequest,
    CompareResponse,
    RecommendationRequest,
    RecommendationResponse,
)
from app.services.comparison import compare_neighborhoods
from app.services.recommendations import get_recommendations_for_business_type

router = APIRouter(tags=["recommendations"])


@router.post("/recommendations", response_model=list[RecommendationResponse])
def get_recommendations(
    request: RecommendationRequest,
) -> list[dict[str, object]]:
    try:
        return get_recommendations_for_business_type(request.business_type_id)
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@router.post("/compare", response_model=CompareResponse)
def compare(
    request: CompareRequest,
) -> dict[str, object]:
    try:
        return compare_neighborhoods(
            request.business_type,
            request.neighborhood_a,
            request.neighborhood_b,
        )
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error