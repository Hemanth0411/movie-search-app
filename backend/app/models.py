from pydantic import BaseModel
from typing import List, Optional

class Movie(BaseModel):
    title: str
    overview: str
    genre: str
    release_date: str
    rating: float
    score: Optional[float] = None

class SearchResponse(BaseModel):
    total: int
    results: List[Movie]
