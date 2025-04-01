from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class Organization(BaseModel):
    """
    A legal or administrative body, institution, or company, or any of its divisions.
    """
    organization_pk: str = Field(..., description="Primary key of the Organization")
    name: str = Field(..., description="Name of the organization")
    description: Optional[str] = Field(None, description="Description of the organization")
    parent_organization_id: Optional[str] = Field(None, description="ID of the parent organization if applicable")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        schema_extra = {
            "example": {
                "organization_pk": "namespace:master-data--Organization:12345",
                "name": "Example Corporation",
                "description": "A global company focused on sustainability",
                "parent_organization_id": None,
                "created_at": "2025-04-01T00:00:00Z",
                "updated_at": "2025-04-01T01:00:00Z"
            }
        }
