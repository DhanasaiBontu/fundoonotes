from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from src.app.api.v1 import api_router
from src.app.core.logger import logger



app = FastAPI(
    title="FundooNotes API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(api_router, prefix="/api/v1")


@app.on_event("startup")
def startup_event():
    logger.info("FundooNotes application started")


@app.on_event("shutdown")
def shutdown_event():
    logger.info("FundooNotes application stopped")


@app.get("/health")
def health():
    logger.info("Health check endpoint called")
    return {"status": "ok"}
