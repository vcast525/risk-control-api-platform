"""
Seed script for creating realistic sample control records.
"""
from sqlalchemy import select

from app.database.config import SessionLocal
from app.models.control import Control



sample_controls = [
    {
        "control_name": "User Access Review",
        "control_owner": "Identity & Access Management",
        "frequency": "Quarterly",
        "status": "Active",
        "description": "Review user access for critical applications on a quarterly basis.",
    },
    {
        "control_name": "Privileged Access Monitoring",
        "control_owner": "Information Security",
        "frequency": "Monthly",
        "status": "Active",
        "description": "Monitor privileged account activity for unauthorized access.",
    },
    {
        "control_name": "Change Approval Review",
        "control_owner": "Change Management",
        "frequency": "Weekly",
        "status": "Active",
        "description": "Review technology changes for documented approvals.",
    },
    {
        "control_name": "Vendor Risk Assessment",
        "control_owner": "Third-Party Risk",
        "frequency": "Annually",
        "status": "Active",
        "description": "Assess third-party vendors for risk and compliance requirements.",
    },
    {
        "control_name": "Business Continuity Plan Review",
        "control_owner": "Business Continuity",
        "frequency": "Annually",
        "status": "Inactive",
        "description": "Review business continuity plans for operational resilience.",
    },
]

owners = [
    "Identity & Access Management",
    "Information Security",
    "Change Management",
    "Third-Party Risk",
    "Business Continuity",
    "Data Governance",
    "Cybersecurity",
    "Operational Risk",
    "Regulatory Compliance",
    "Technology Risk",
]

frequencies = ["Daily", "Weekly", "Monthly", "Quarterly", "Annually"]

statuses = ["Active", "Active", "Active", "Inactive"]

control_templates = [
    "Access Certification Review",
    "System Monitoring Control",
    "Data Quality Validation",
    "Incident Response Review",
    "Application Change Review",
]


for index in range(1, 51):
    sample_controls.append(
        {
            "control_name": f"{control_templates[index % len(control_templates)]} {index}",
            "control_owner": owners[index % len(owners)],
            "frequency": frequencies[index % len(frequencies)],
            "status": statuses[index % len(statuses)],
            "description": f"Sample control record {index} used for API filtering and pagination testing.",
        }
    )

def seed_controls():
    """
    Insert sample control records into the local development database.
    """
    db = SessionLocal()

    try:
        for control_data in sample_controls:
            statement = select(Control).where(
                Control.control_name == control_data["control_name"],
                Control.control_owner == control_data["control_owner"],
            )

            existing_control = db.scalar(statement)

            if existing_control:
                continue

            control = Control(**control_data)
            db.add(control)

        db.commit()
        print("Sample control records seeded successfully.")

    finally:
        db.close()

if __name__ == "__main__":
    seed_controls()