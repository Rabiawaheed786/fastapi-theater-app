# routes\review_routes.py
from typing import List
from fastapi import APIRouter, Depends
from src.utils.api_response import ReviewResponse
from src.utils.exception import InvalidReviewError
from src.interface.review_create_interface import ReviewCreate
from sqlmodel import Session, select
from src.db.engine import get_session
from src.model.model import Review

import rich



router = APIRouter(prefix="/reviews", tags=["/reviews"])


# POST localhost:8000/reviews
@router.post("/", response_model=Review)
def create_review(review: ReviewCreate, session: Session = Depends(get_session)):

    data_dic = Review.model_validate(review) # creating Dic by json object

    session.add(data_dic) # database me insert kar diya
    session.commit() # save into database
    session.refresh(data_dic) # updating Dic with id

    return data_dic

# ------------------------------------------------------------------

# GET localhost:8000/reviews
@router.get("/", response_model=ReviewResponse)
def list_reviews(play_name: str | None = None, session: Session = Depends(get_session)):

    if play_name:
        statement = select(Review).where(Review.play_name == play_name)
    else:
        statement = select(Review)
    result = session.exec(statement) # to execute select query into database
    reviews = result.all() # to extract all entries of Review table

    if not reviews:
        raise InvalidReviewError(404, play_name or "", f"No data found for {play_name}")

    return ReviewResponse(count=len(reviews), items=list(reviews))