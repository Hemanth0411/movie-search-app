from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import os

app = FastAPI(title="Movie Search App")

class Health(BaseModel):
    status: str

@app.get("/health", response_model=Health)
async def health_check():
    return JSONResponse(content={"status": "ok"})

@app.get("/")
def root():
    return {"message": "Movie Search backend running"}
