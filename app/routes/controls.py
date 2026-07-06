"""
API routes for control-related operations.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.config import get_db
from app.schemas.control import ControlCreate
from app.services.control_service import create_control


router = APIRouter(
    prefix="/controls",
    tags=["Controls"],
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_control_route(
    control: ControlCreate,
    db: Session = Depends(get_db),
):
    """
    Receive and direct a request to create a new control.
    """
    return create_control(db=db, control=control)