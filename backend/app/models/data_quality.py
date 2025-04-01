from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class DataQualityBase(BaseModel):
    """
    Entities for verifying and ensuring quality of emissions data.
    """
    quality_score: Optional[float] = Field(None, description="Quality score of the data (0-100)")
    verification_status: Optional[str] = Field(None, description="Status of verification (e.g., 'Verified', 'Pending', 'Rejected')")
    verification_date: Optional[datetime] = Field(None, description="Date when the data was verified")
    verified_by: Optional[str] = Field(None, description="Person or organization who verified the data")
    notes: Optional[str] = Field(None, description="Additional notes about data quality")

class DataQualityCreate(DataQualityBase):
    entity_id: str = Field(..., description="ID of the entity this quality assessment belongs to")

class DataQuality(DataQualityBase):
    entity_id: str = Field(..., description="ID of the entity this quality assessment belongs to")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "entity_id": "namespace:transactional-data--EmissionStatement:12345",
                "quality_score": 85.5,
                "verification_status": "Verified",
                "verification_date": "2025-03-15T00:00:00Z",
                "verified_by": "EcoVerify Inc.",
                "notes": "Data verified through third-party audit",
                "created_at": "2025-04-01T00:00:00Z",
                "updated_at": "2025-04-01T01:00:00Z"
            }
        }
