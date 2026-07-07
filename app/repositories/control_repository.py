"""
Database operations for control records.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.control import Control
from app.schemas.control import ControlCreate, ControlUpdate


def get_active_control_by_name_and_owner(
    db: Session,
    control_name: str,
    control_owner: str,
) -> Control | None:
    """
    Retrieve an active control with the same name and owner, if one exists.
    """
    statement = select(Control).where(
        Control.control_name == control_name,
        Control.control_owner == control_owner,
        Control.status == "Active",
    )

    return db.scalar(statement)

def create_control(
    db: Session,
    control: ControlCreate,
) -> Control:
    """
    Create and persist a new control record.
    """
    db_control = Control(
        control_name=control.control_name,
        control_owner=control.control_owner,
        frequency=control.frequency.value,
        status=control.status.value,
        description=control.description,
    )

    db.add(db_control)
    db.commit()
    db.refresh(db_control)

    return db_control

def get_all_controls(db: Session) -> list[Control]:
    """
    Retrieve all control records.
    """
    statement = select(Control)

    return list(db.scalars(statement).all())

def get_control_by_id(
    db: Session,
    control_id: int,
) -> Control | None:
    """
    Retrieve a control record by its unique identifier.
    """
    return db.get(Control, control_id)

def update_control(
    db: Session,
    db_control: Control,
    control_update: ControlUpdate,
) -> Control:
    """
    Update an existing control record.
    """
    update_data = control_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        if hasattr(value, "value"):
            value = value.value

        setattr(db_control, field, value)

    db.commit()
    db.refresh(db_control)

    return db_control

def deactivate_control(
    db: Session,
    db_control: Control,
) -> Control:
    """
    Deactivate an existing control record.
    """
    db_control.status = "Inactive"

    db.commit()
    db.refresh(db_control)

    return db_control