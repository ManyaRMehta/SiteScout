from sqlalchemy.orm import Session

from app.data.mock_data import BUSINESS_TYPES, BUSINESS_TYPE_WEIGHTS, NEIGHBORHOOD_SCORES
from app.db.models import BusinessType, Neighborhood
from app.db.session import SessionLocal, create_database_tables


def seed_business_types(db: Session) -> None:
    for business_type in BUSINESS_TYPES:
        business_type_id = business_type["id"]
        weights = BUSINESS_TYPE_WEIGHTS[business_type_id]

        db.merge(
            BusinessType(
                id=business_type_id,
                name=business_type["name"],
                demand_weight=weights["demand"],
                competition_weight=weights["competition"],
                affordability_weight=weights["affordability"],
                transit_weight=weights["transit"],
                growth_weight=weights["growth"],
            )
        )


def seed_neighborhoods(db: Session) -> None:
    for neighborhood in NEIGHBORHOOD_SCORES:
        scores = neighborhood["scores"]

        db.merge(
            Neighborhood(
                id=neighborhood["id"],
                name=neighborhood["name"],
                demand_score=scores["demand"],
                competition_score=scores["competition"],
                affordability_score=scores["affordability"],
                transit_score=scores["transit"],
                growth_score=scores["growth"],
            )
        )


def seed_database() -> None:
    create_database_tables()

    db = SessionLocal()
    try:
        seed_business_types(db)
        seed_neighborhoods(db)
        db.commit()
        print("Seeded SiteScout database successfully.")
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()