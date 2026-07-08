from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    business_type_id: str


class CategoryScores(BaseModel):
    demand: float
    competition: float
    affordability: float
    transit: float
    growth: float


class RecommendationResponse(BaseModel):
    id: str
    name: str
    overall_score: float
    category_scores: CategoryScores
    explanation: str