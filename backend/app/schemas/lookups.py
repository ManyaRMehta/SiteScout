from pydantic import BaseModel


class BusinessType(BaseModel):
    id: str
    name: str


class Neighborhood(BaseModel):
    id: str
    name: str
