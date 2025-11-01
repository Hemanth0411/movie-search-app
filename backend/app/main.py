from fastapi import FastAPI, Query
from services.search_services import search_movies
from app.models import SearchResponse

app = FastAPI(title="Movie Search - Mini")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Movie Search backend running"}

@app.get("/search", response_model=SearchResponse)
def search(
    q: str = Query(..., description="Search text"),
    genre: str = Query(None, description="Optional genre filter"),
    sort: str = Query("relevance", regex="^(relevance|rating)$"),
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=50)
):
    return search_movies(q, genre, sort, page, size)
