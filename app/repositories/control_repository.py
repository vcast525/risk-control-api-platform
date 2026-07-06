"""
Database operations for control records.
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.control import Control
from app.schemas.control import ControlCreate


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