from sqlalchemy import Float, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.session import Base


class BusinessType(Base):
    __tablename__ = "business_types"

    id: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    demand_weight: Mapped[float] = mapped_column(Float, nullable=False)
    competition_weight: Mapped[float] = mapped_column(Float, nullable=False)
    affordability_weight: Mapped[float] = mapped_column(Float, nullable=False)
    transit_weight: Mapped[float] = mapped_column(Float, nullable=False)
    growth_weight: Mapped[float] = mapped_column(Float, nullable=False)


class Neighborhood(Base):
    __tablename__ = "neighborhoods"

    id: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    demand_score: Mapped[float] = mapped_column(Float, nullable=False)
    competition_score: Mapped[float] = mapped_column(Float, nullable=False)
    affordability_score: Mapped[float] = mapped_column(Float, nullable=False)
    transit_score: Mapped[float] = mapped_column(Float, nullable=False)
    growth_score: Mapped[float] = mapped_column(Float, nullable=False)