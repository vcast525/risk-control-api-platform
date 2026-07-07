"""
SQLAlchemy model for control records.
"""

from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.config import Base


class Control(Base):
    """
    Database model representing a risk control record.
    """

    __tablename__ = "controls"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    control_name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    control_owner: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    frequency: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default="Active")
    description: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )