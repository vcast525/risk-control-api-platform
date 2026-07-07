"""
Seed sample application users into the PostgreSQL database.
"""

from app.database.config import SessionLocal
from app.models.user import User


sample_users = [
    {
        "first_name": "Maria",
        "last_name": "Chen",
        "email": "maria.chen@example.com",
        "role": "Control Owner",
        "department": "Technology Risk",
        "status": "Active",
    },
    {
        "first_name": "David",
        "last_name": "Thompson",
        "email": "david.thompson@example.com",
        "role": "Risk Analyst",
        "department": "Enterprise Risk",
        "status": "Active",
    },
    {
        "first_name": "Sarah",
        "last_name": "Williams",
        "email": "sarah.williams@example.com",
        "role": "Control Manager",
        "department": "Operational Risk",
        "status": "Active",
    },
    {
        "first_name": "James",
        "last_name": "Rodriguez",
        "email": "james.rodriguez@example.com",
        "role": "Administrator",
        "department": "Risk Technology",
        "status": "Active",
    },
    {
        "first_name": "Vincent",
        "last_name": "Castillo",
        "email": "vincent.castillo@example.com",
        "role": "Risk Analyst",
        "department": "Controls Governance",
        "status": "Active",
    },
]


def seed_users():
    """
    Insert sample application users into the database.
    """
    db = SessionLocal()

    try:
        for user_data in sample_users:
            existing_user = (
                db.query(User)
                .filter(User.email == user_data["email"])
                .first()
            )

            if existing_user:
                continue

            user = User(**user_data)
            db.add(user)

        db.commit()
        print("Sample application users seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    seed_users()