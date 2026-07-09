from pydantic import BaseModel


class BusinessTypeResponse(BaseModel):
    id: str
    name: str


class NeighborhoodResponse(BaseModel):
    id: str
    name: str