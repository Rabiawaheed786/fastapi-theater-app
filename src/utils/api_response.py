from typing import List
from sqlmodel import SQLModel
from src.model.model import Review


class ReviewResponse(SQLModel):
    status: str = "success"
    count: int
    items: List[Review]


# ----------------------------------------


class AvgResponse(SQLModel):
    play_name: str
    avg_rating: int
    total_reviews: int


class ReviewAvgResponse(SQLModel):
    status: str = "success"
    count: int
    items: AvgResponse