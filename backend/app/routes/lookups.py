from fastapi import APIRouter

from app.data.mock_data import BUSINESS_TYPES, NEIGHBORHOODS
from app.schemas.lookups import BusinessType, Neighborhood

router = APIRouter(tags=["lookups"])


@router.get("/business-types", response_model=list[BusinessType])
def get_business_types() -> list[dict[str, str]]:
    return BUSINESS_TYPES


@router.get("/neighborhoods", response_model=list[Neighborhood])
def get_neighborhoods() -> list[dict[str, str]]:
    return NEIGHBORHOODS
