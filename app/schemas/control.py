"""
Pydantic schemas for control-related API requests and responses.
"""

from enum import Enum
from pydantic import BaseModel, Field


class ControlFrequency(str, Enum):
    daily = "Daily"
    weekly = "Weekly"
    monthly = "Monthly"
    quarterly = "Quarterly"
    annually = "Annually"


class ControlStatus(str, Enum):
    active = "Active"
    inactive = "Inactive"


class ControlCreate(BaseModel):
    control_name: str = Field(..., min_length=3, max_length=100)
    control_owner: str = Field(..., min_length=2, max_length=100)
    frequency: ControlFrequency
    status: ControlStatus = ControlStatus.active
    description: str | None = Field(default=None, max_length=500)