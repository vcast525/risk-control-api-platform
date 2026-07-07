"""
Pydantic schemas for control-related API requests and responses.
"""

from enum import Enum
from pydantic import BaseModel, Field
from datetime import datetime

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

class ControlUpdate(BaseModel):
    control_name: str | None = Field(
        default=None,
        min_length=3,
        max_length=100,
    )
    control_owner: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )
    frequency: ControlFrequency | None = None
    status: ControlStatus | None = None
    description: str | None = Field(
        default=None,
        max_length=500,
    )

class UserAuditResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    role: str
    department: str

    model_config = {
        "from_attributes": True
    }

class ControlResponse(BaseModel):
    id: int
    control_name: str
    control_owner: str
    frequency: ControlFrequency
    status: ControlStatus
    description: str | None
    created_at: datetime
    updated_at: datetime
    created_by_id: int | None
    updated_by_id: int | None
    created_by: UserAuditResponse | None
    updated_by: UserAuditResponse | None
    model_config = {
        "from_attributes": True
    }

class ControlListResponse(BaseModel):
    message: str
    count: int
    total: int
    offset: int
    limit: int
    controls: list[ControlResponse]

class SingleControlResponse(BaseModel):
    message: str
    control: ControlResponse