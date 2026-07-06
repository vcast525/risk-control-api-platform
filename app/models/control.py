"""
SQLAlchemy model for control records.
"""

from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database.config import Base


class Control(Base):
    """
    Database model representing a risk control record.
    """

    __tablename__ = "controls"

    id = Column(Integer, primary_key=True, index=True)
    control_name = Column(String(100), nullable=False, index=True)
    control_owner = Column(String(100), nullable=False, index=True)
    frequency = Column(String(50), nullable=False)
    status = Column(String(50), nullable=False, default="Active")
    description = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)