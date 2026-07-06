"""
Risk Control API Platform

Application entry point for the FastAPI backend.
"""

from fastapi import FastAPI

from app.database.config import Base, engine
from app.models import control
from app.routes.controls import router as controls_router


app = FastAPI(
    title="Risk Control API Platform",
    description=(
        "A backend REST API for managing risk controls, "
        "assessments, issues, and remediation workflows."
    ),
    version="0.1.0",
)

# Create the database tables
Base.metadata.create_all(bind=engine)

app.include_router(controls_router)

@app.get("/")
def read_root():
    """
    Root endpoint used to confirm that the API is running.
    """
    return {
        "message": "Risk Control API Platform is running",
        "status": "success",
        "version": "0.1.0",
    }