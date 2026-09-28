from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from src.db.engine import create_tables
from src.routes.review_routes import router as review_router
from src.utils.exception import InvalidReviewError, invalid_review_error_handler

# control you starting and ending of server
@asynccontextmanager
async def lifespan(params: FastAPI):
    print("✅ server start ho gaya")
    create_tables()
    yield
    print("❌ server stop ho gaya")

app = FastAPI(
    title="Theater App Backend",
    description="backend Api of reviews for Theater App",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception class register in fastApi
app.add_exception_handler(InvalidReviewError, invalid_review_error_handler)

app.include_router(review_router)

@app.get("/")
def hello():
    index_path = Path(__file__).parent / "index.html"
    if index_path.exists():
        return FileResponse(index_path)
    return {"message" : "hello i am here!"}