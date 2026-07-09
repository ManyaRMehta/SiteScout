from sqlalchemy.orm import Session

from app.db.models import BusinessType, Neighborhood


def get_business_types(db: Session) -> list[dict[str, str]]:
    business_types = db.query(BusinessType).order_by(BusinessType.name).all()

    return [
        {
            "id": business_type.id,
            "name": business_type.name,
        }
        for business_type in business_types
    ]


def get_neighborhoods(db: Session) -> list[dict[str, str]]:
    neighborhoods = db.query(Neighborhood).order_by(Neighborhood.name).all()

    return [
        {
            "id": neighborhood.id,
            "name": neighborhood.name,
        }
        for neighborhood in neighborhoods
    ]