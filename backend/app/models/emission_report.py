from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID

class EmissionReport(BaseModel):
    """
    A document that describes the organization emission inventory and emissions over a period time.
    
    Recommended as per ISO 14064-1 GHG Report Content and other standards.
    """
    emission_report_pk: str = Field(..., description="Primary key of the Emission Report")
    description: Optional[str] = Field(None, description="A long description of the Emission Report")
    report_period_start: datetime = Field(..., description="Start date of the reporting period")
    report_period_end: datetime = Field(..., description="End date of the reporting period")
    organization_id: str = Field(..., description="ID of the organization this report belongs to")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        schema_extra = {
            "example": {
                "emission_report_pk": "namespace:transactional-data--EmissionReport:12345",
                "description": "Annual GHG emissions report for 2024",
                "report_period_start": "2024-01-01T00:00:00Z",
                "report_period_end": "2024-12-31T23:59:59Z",
                "organization_id": "namespace:master-data--Organization:67890",
                "created_at": "2025-04-01T00:00:00Z",
                "updated_at": "2025-04-01T01:00:00Z"
            }
        }
