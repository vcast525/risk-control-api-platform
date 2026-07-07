"""
Assign existing controls to seeded application users.
"""

from sqlalchemy import select

from app.database.config import SessionLocal
from app.models.control import Control
from app.models.user import User


def assign_control_users():
    """
    Assign created_by_id and updated_by_id values to existing controls.
    """
    db = SessionLocal()

    try:
        users = list(db.scalars(select(User).order_by(User.id)).all())
        controls = list(db.scalars(select(Control).order_by(Control.id)).all())

        if not users:
            raise RuntimeError("No users found. Run seed_users.py first.")

        for index, control in enumerate(controls):
            created_by_user = users[index % len(users)]
            updated_by_user = users[(index + 1) % len(users)]

            control.created_by_id = created_by_user.id
            control.updated_by_id = updated_by_user.id

        db.commit()
        print(f"Assigned users to {len(controls)} controls.")

    finally:
        db.close()


if __name__ == "__main__":
    assign_control_users()