"""
API routes for control-related operations.
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.config import get_db
from app.schemas.control import (
    ControlCreate,
    ControlListResponse,
    ControlUpdate,
    SingleControlResponse,
)
from app.services.control_service import (
    create_control,
    retrieve_control_by_id,
    retrieve_controls,
    update_control,
    deactivate_control,
)


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

@router.get("/", response_model=ControlListResponse)
def get_controls_route(db: Session = Depends(get_db)):
    """
    Retrieve all control records.
    """
    return retrieve_controls(db=db)

@router.get("/{control_id}", response_model=SingleControlResponse)
def get_control_by_id_route(
    control_id: int,
    db: Session = Depends(get_db),
):
    """
    Retrieve a single control record by ID.
    """
    return retrieve_control_by_id(db=db, control_id=control_id)

@router.patch("/{control_id}", response_model=SingleControlResponse)
def update_control_route(
    control_id: int,
    control_update: ControlUpdate,
    db: Session = Depends(get_db),
):
    """
    Update an existing control record.
    """
    return update_control(
        db=db,
        control_id=control_id,
        control_update=control_update,
    )

@router.patch("/{control_id}/deactivate", response_model=SingleControlResponse)
def deactivate_control_route(
    control_id: int,
    db: Session = Depends(get_db),
):
    """
    Deactivate an existing control record.
    """
    return deactivate_control(db=db, control_id=control_id)