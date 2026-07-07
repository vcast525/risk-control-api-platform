"""
Business logic for control-related operations.
"""

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories.control_repository import (
    create_control as create_control_record,
    get_active_control_by_name_and_owner,
    get_all_controls,
    get_control_by_id,
    update_control as update_control_record,
    deactivate_control as deactivate_control_record,
)

from app.schemas.control import ControlCreate, ControlUpdate


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

def retrieve_controls(
    db: Session,
    status_filter: str | None = None,
    control_owner: str | None = None,
    frequency: str | None = None,
) -> dict:
    """
    Retrieve control records with optional filters.
    """
    controls = get_all_controls(
        db=db,
        status=status_filter,
        control_owner=control_owner,
        frequency=frequency,
    )

    return {
        "message": "Controls retrieved successfully",
        "count": len(controls),
        "controls": controls,
    }

def retrieve_control_by_id(db: Session, control_id: int) -> dict:
    """
    Retrieve a single control record by ID.
    """
    control = get_control_by_id(db=db, control_id=control_id)

    if control is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Control record not found.",
        )

    return {
        "message": "Control retrieved successfully",
        "control": control,
    }

def update_control(
    db: Session,
    control_id: int,
    control_update: ControlUpdate,
) -> dict:
    """
    Update an existing control record.
    """
    control = get_control_by_id(db=db, control_id=control_id)

    if control is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Control record not found.",
        )

    updated_control = update_control_record(
        db=db,
        db_control=control,
        control_update=control_update,
    )

    return {
        "message": "Control updated successfully",
        "control": updated_control,
    }

def deactivate_control(db: Session, control_id: int) -> dict:
    """
    Deactivate an existing control record.
    """
    control = get_control_by_id(db=db, control_id=control_id)

    if control is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Control record not found.",
        )

    if control.status == "Inactive":
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Control record is already inactive.",
        )

    deactivated_control = deactivate_control_record(
        db=db,
        db_control=control,
    )

    return {
        "message": "Control deactivated successfully",
        "control": deactivated_control,
    }