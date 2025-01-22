from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Todo API",
    version="/api/v1"
)

@app.get("/")
def root():
    return {"message": "Hello API"}
