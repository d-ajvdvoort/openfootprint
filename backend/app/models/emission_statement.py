from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any, Union
from datetime import datetime

class EmissionStatementBase(BaseModel):
    """
    A quantification of the release or removal of an emission into or from the atmosphere that is recorded.
    
    Based on ISO 14064-1, but not constrained to GHG only.
    """
    emission_activity_id: str = Field(..., description="Foreign key of the Emission Activity")
    emission_calculation_model_id: Optional[str] = Field(None, description="The foreign key of the Emission Calculation Model")
    value: float = Field(..., description="The quantified value of the emission")
    unit: str = Field(..., description="The unit of measurement for the emission value")
    reporting_period_start: datetime = Field(..., description="Start date of the reporting period")
    reporting_period_end: datetime = Field(..., description="End date of the reporting period")
    facility_id: Optional[str] = Field(None, description="ID of the facility where the emission occurred")
    organization_id: str = Field(..., description="ID of the organization responsible for the emission")

class EmissionStatementCreate(EmissionStatementBase):
    emission_statement_pk: str = Field(..., description="Primary key of the Emission Statement")

class EmissionStatement(EmissionStatementBase):
    emission_statement_pk: str = Field(..., description="Primary key of the Emission Statement")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "emission_statement_pk": "namespace:transactional-data--EmissionStatement:12345",
                "emission_activity_id": "namespace:master-data--EmissionActivity:67890",
                "emission_calculation_model_id": "namespace:master-data--EmissionCalculationModel:54321",
                "value": 1250.5,
                "unit": "kg CO2e",
                "reporting_period_start": "2024-01-01T00:00:00Z",
                "reporting_period_end": "2024-01-31T23:59:59Z",
                "facility_id": "namespace:master-data--Facility:12345",
                "organization_id": "namespace:master-data--Organization:67890",
                "created_at": "2025-04-01T00:00:00Z",
                "updated_at": "2025-04-01T01:00:00Z"
            }
        }
