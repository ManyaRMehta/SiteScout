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


class CompareRequest(BaseModel):
    business_type: str
    neighborhood_a: str
    neighborhood_b: str


class ComparedNeighborhood(BaseModel):
    id: str
    name: str
    overall_score: float
    category_scores: CategoryScores
    explanation: str


class CompareResponse(BaseModel):
    business_type: str
    neighborhood_a: ComparedNeighborhood
    neighborhood_b: ComparedNeighborhood
    winner: str
    summary: str


class WhatIfRequest(BaseModel):
    business_type_id: str
    custom_weights: CategoryScores


class WhatIfRecommendationResponse(BaseModel):
    id: str
    name: str
    previous_rank: int
    new_rank: int
    rank_change: int
    overall_score: float
    category_scores: CategoryScores
    explanation: str


class WhatIfResponse(BaseModel):
    business_type_id: str
    custom_weights: CategoryScores
    recommendations: list[WhatIfRecommendationResponse]
    summary: str