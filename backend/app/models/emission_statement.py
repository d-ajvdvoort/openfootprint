from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import UUID

class EmissionStatement(BaseModel):
    """
    A quantification of the release or removal of an emission into or from the atmosphere that is recorded.
    
    Based on ISO 14064-1, but not constrained to GHG only.
    """
    emission_statement_pk: str = Field(..., description="Primary key of the Emission Statement")
    emission_activity_id: str = Field(..., description="Foreign key of the Emission Activity")
    emission_calculation_model_id: Optional[str] = Field(None, description="The foreign key of the Emission Calculation Model")
    created_at: datetime = Field(default_factory=datetime.now, description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        schema_extra = {
            "example": {
                "emission_statement_pk": "namespace:transactional-data--EmissionStatement:12345",
                "emission_activity_id": "namespace:master-data--EmissionActivity:67890",
                "emission_calculation_model_id": "namespace:master-data--EmissionCalculationModel:54321",
                "created_at": "2025-04-01T00:00:00Z",
                "updated_at": "2025-04-01T01:00:00Z"
            }
        }
