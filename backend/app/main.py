from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI(title="Movie Search App")

class Health(BaseModel):
    status: str

@app.get("/health", response_model=Health)
def health():
    return Health(status="ok")

@app.get("/")
def root():
    return {"message": "Movie Search backend running"}
