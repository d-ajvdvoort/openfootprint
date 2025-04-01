from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class FacilityBase(BaseModel):
    """
    A physical location where emissions occur.
    """
    name: str = Field(..., description="Name of the facility")
    description: Optional[str] = Field(None, description="Description of the facility")
    address: Optional[str] = Field(None, description="Address of the facility")
    city: Optional[str] = Field(None, description="City where the facility is located")
    country: Optional[str] = Field(None, description="Country where the facility is located")
    latitude: Optional[float] = Field(None, description="Latitude coordinate of the facility")
    longitude: Optional[float] = Field(None, description="Longitude coordinate of the facility")

class FacilityCreate(FacilityBase):
    facility_pk: str = Field(..., description="Primary key of the Facility")

class Facility(FacilityBase):
    facility_pk: str = Field(..., description="Primary key of the Facility")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "facility_pk": "namespace:master-data--Facility:12345",
                "name": "Manufacturing Plant Alpha",
                "description": "Main manufacturing facility for consumer products",
                "address": "123 Industrial Way",
                "city": "Springfield",
                "country": "United States",
                "latitude": 37.7749,
                "longitude": -122.4194,
                "created_at": "2025-04-01T00:00:00Z",
                "updated_at": "2025-04-01T01:00:00Z"
            }
        }
