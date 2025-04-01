from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class WaterActivityTypeBase(BaseModel):
    """
    Categorizes water-related activities.
    """
    water_activity_type_name: str = Field(..., description="Name of the water activity type")
    description: Optional[str] = Field(None, description="Description of the water activity type")

class WaterActivityTypeCreate(WaterActivityTypeBase):
    water_activity_type_id: str = Field(..., description="ID of the water activity type")

class WaterActivityType(WaterActivityTypeBase):
    water_activity_type_id: str = Field(..., description="ID of the water activity type")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "water_activity_type_id": "namespace:master-data--WaterActivityType:12345",
                "water_activity_type_name": "Water Withdrawal",
                "description": "Extraction of water from any source",
                "created_at": "2025-04-01T00:00:00Z",
                "updated_at": "2025-04-01T01:00:00Z"
            }
        }
