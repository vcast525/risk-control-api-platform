"""
Generate large-scale sample control records for performance testing.
"""
from sqlalchemy import select

from app.database.config import SessionLocal
from app.models.control import Control
from app.models.user import User

TOTAL_RECORDS = 100_000
BATCH_SIZE = 5_000

CONTROL_TEMPLATES = [
    "Access Certification Review",
    "Privileged Access Monitoring",
    "Change Approval Validation",
    "Data Quality Reconciliation",
    "Incident Response Review",
    "Vendor Risk Assessment",
    "Business Continuity Validation",
    "Regulatory Reporting Control",
    "Application Security Review",
    "Change Management Approval",
]

CONTROL_OWNERS = [
    "Technology Risk",
    "Information Security",
    "Operational Risk",
    "Data Governance",
    "Third-Party Risk",
    "Business Continuity",
    "Regulatory Compliance",
    "Identity & Access Management",
]

FREQUENCIES = ["Daily", "Weekly", "Monthly", "Quarterly", "Annually"]

STATUSES = ["Active", "Active", "Active", "Inactive"]

def seed_large_controls():
    """
    Generate and insert large-scale control records in batches.
    """
    db = SessionLocal()

    try:
        users = list(
            db.scalars(
                select(User).order_by(User.id)
            ).all()
        )

        if not users:
            raise RuntimeError("No users found. Run seed_users.py first.")

        for start in range(1, TOTAL_RECORDS + 1, BATCH_SIZE):
            end = min(start + BATCH_SIZE, TOTAL_RECORDS + 1)

            batch = []

            for index in range(start, end):
                created_by_user = users[index % len(users)]
                updated_by_user = users[(index + 1) % len(users)]

                control = Control(
                    control_name=f"{CONTROL_TEMPLATES[index % len(CONTROL_TEMPLATES)]} {index}",
                    control_owner=CONTROL_OWNERS[index % len(CONTROL_OWNERS)],
                    frequency=FREQUENCIES[index % len(FREQUENCIES)],
                    status=STATUSES[index % len(STATUSES)],
                    description=f"Large-scale generated control record {index}.",
                    created_by_id=created_by_user.id,
                    updated_by_id=updated_by_user.id,
                )

                batch.append(control)

            db.add_all(batch)
            db.commit()

            print(f"Inserted records {start} through {end - 1}.")

        print(f"Large-scale seeding complete: {TOTAL_RECORDS} records inserted.")

    finally:
        db.close()

if __name__ == "__main__":
    seed_large_controls()