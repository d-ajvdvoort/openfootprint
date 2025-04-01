from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

class CSRDReportType(str, Enum):
    ANNUAL = "Annual"
    INTERIM = "Interim"
    SUPPLEMENTARY = "Supplementary"

class CSRDReportStatus(str, Enum):
    DRAFT = "Draft"
    IN_REVIEW = "In Review"
    APPROVED = "Approved"
    PUBLISHED = "Published"
    SUBMITTED = "Submitted"

class CSRDReportBase(BaseModel):
    """
    A CSRD (Corporate Sustainability Reporting Directive) compliant report.
    """
    title: str = Field(..., description="Title of the CSRD report")
    description: Optional[str] = Field(None, description="Description of the CSRD report")
    reporting_period_start: datetime = Field(..., description="Start date of the reporting period")
    reporting_period_end: datetime = Field(..., description="End date of the reporting period")
    organization_id: str = Field(..., description="ID of the organization this report belongs to")
    report_type: CSRDReportType = Field(..., description="Type of CSRD report")
    status: CSRDReportStatus = Field(..., description="Status of the CSRD report")
    version: str = Field(..., description="Version of the report")
    prepared_by: str = Field(..., description="Person or entity who prepared the report")
    approved_by: Optional[str] = Field(None, description="Person or entity who approved the report")

class CSRDReportCreate(CSRDReportBase):
    csrd_report_pk: str = Field(..., description="Primary key of the CSRD Report")
    emission_report_ids: List[str] = Field(..., description="List of emission report IDs included in this CSRD report")

class CSRDReport(CSRDReportBase):
    csrd_report_pk: str = Field(..., description="Primary key of the CSRD Report")
    emission_report_ids: List[str] = Field(..., description="List of emission report IDs included in this CSRD report")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")
    
    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "csrd_report_pk": "namespace:transactional-data--CSRDReport:12345",
                "title": "Annual CSRD Compliance Report 2024",
                "description": "Comprehensive sustainability report following CSRD requirements",
                "reporting_period_start": "2024-01-01T00:00:00Z",
                "reporting_period_end": "2024-12-31T23:59:59Z",
                "organization_id": "namespace:master-data--Organization:67890",
                "report_type": "Annual",
                "status": "Draft",
                "version": "1.0",
                "prepared_by": "Sustainability Department",
                "approved_by": None,
                "emission_report_ids": [
                    "namespace:transactional-data--EmissionReport:12345",
                    "namespace:transactional-data--EmissionReport:12346"
                ],
                "created_at": "2025-04-01T00:00:00Z",
                "updated_at": None
            }
        }
