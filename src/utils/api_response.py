from typing import List
from sqlmodel import SQLModel
from src.model.model import Review



class ReviewResponse(SQLModel):
    status: str = "success"
    count: int
    items: List[Review]