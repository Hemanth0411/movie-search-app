from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.models import SearchResponse
from services.search_services import search_movies  # ✅ Import added

app = FastAPI(title="Movie Search - Mini")


class Health(BaseModel):
    status: str


@app.get("/health", response_model=Health)
async def health_check():
    return JSONResponse(content={"status": "ok"})


@app.get("/")
def root():
    return {"message": "Movie Search backend running"}


q_query = Query(..., description="Search text")
genre_query = Query(None, description="Optional genre filter")
sort_query = Query("relevance", pattern="^(relevance|rating)$")
page_query = Query(1, ge=1)
size_query = Query(10, ge=1, le=50)


@app.get("/search", response_model=SearchResponse)
def search(
    q: str = q_query,
    genre: str = genre_query,
    sort: str = sort_query,
    page: int = page_query,
    size: int = size_query,
):
    return search_movies(q, genre, sort, page, size)
