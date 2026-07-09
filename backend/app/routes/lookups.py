from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.lookups import BusinessTypeResponse, NeighborhoodResponse
from app.services.lookups import get_business_types, get_neighborhoods

router = APIRouter(tags=["lookups"])


@router.get("/business-types", response_model=list[BusinessTypeResponse])
def list_business_types(
    db: Session = Depends(get_db),
) -> list[dict[str, str]]:
    return get_business_types(db)


@router.get("/neighborhoods", response_model=list[NeighborhoodResponse])
def list_neighborhoods(
    db: Session = Depends(get_db),
) -> list[dict[str, str]]:
    return get_neighborhoods(db)