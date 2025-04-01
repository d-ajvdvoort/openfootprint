from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class EnvironmentalProductDeclarationBase(BaseModel):
    """
    A document that holds information about a products potential environmental and human health impact.
    
    An Environment Product Declaration (EPD) is also known as a Type III environmental declaration in the ISO 14040 series.
    """
    description: Optional[str] = Field(None, description="Long description of the Environmental Product Declaration")
    product_name: str = Field(..., description="Name of the product")
    organization_id: str = Field(..., description="ID of the organization responsible for the product")
    valid_from: datetime = Field(..., description="Date from which the declaration is valid")
    valid_to: Optional[datetime] = Field(None, description="Date until which the declaration is valid")

class EnvironmentalProductDeclarationCreate(EnvironmentalProductDeclarationBase):
    environmental_product_declaration_pk: str = Field(..., description="Primary key of the Environmental Product Declaration")

class EnvironmentalProductDeclaration(EnvironmentalProductDeclarationBase):
    environmental_product_declaration_pk: str = Field(..., description="Primary key of the Environmental Product Declaration")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "environmental_product_declaration_pk": "namespace:transactional-data--EnvironmentalProductDeclaration:12345",
                "description": "Environmental impact assessment for Product XYZ",
                "product_name": "Product XYZ",
                "organization_id": "namespace:master-data--Organization:67890",
                "valid_from": "2025-01-01T00:00:00Z",
                "valid_to": "2030-01-01T00:00:00Z",
                "created_at": "2025-04-01T00:00:00Z",
                "updated_at": "2025-04-01T01:00:00Z"
            }
        }
