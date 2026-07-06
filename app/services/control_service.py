"""
Business logic for control-related operations.
"""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.control_repository import (
    create_control as create_control_record,
    get_active_control_by_name_and_owner,
)
from app.schemas.control import ControlCreate


def create_control(db: Session, control: ControlCreate) -> dict:
    """
    Process the business logic required to create a control.
    """
    existing_control = get_active_control_by_name_and_owner(
        db=db,
        control_name=control.control_name,
        control_owner=control.control_owner,
    )

    if existing_control:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=(
                "An active control with this name and owner "
                "already exists."
            ),
        )

    created_control = create_control_record(db=db, control=control)

    return {
        "message": "Control created successfully",
        "control": created_control,
    }