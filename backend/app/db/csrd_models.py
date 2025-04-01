from sqlalchemy import Column, String, Float, DateTime, ForeignKey, Table, Integer, Enum, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from enum import Enum as PyEnum

from app.db.database import Base

class CSRDReportType(str, PyEnum):
    ANNUAL = "Annual"
    INTERIM = "Interim"
    SUPPLEMENTARY = "Supplementary"

class CSRDReportStatus(str, PyEnum):
    DRAFT = "Draft"
    IN_REVIEW = "In Review"
    APPROVED = "Approved"
    PUBLISHED = "Published"
    SUBMITTED = "Submitted"

# Association table for many-to-many relationship between CSRDReport and EmissionReport
csrd_emission_reports = Table(
    'csrd_emission_reports',
    Base.metadata,
    Column('csrd_report_pk', String, ForeignKey('csrd_reports.csrd_report_pk')),
    Column('emission_report_pk', String, ForeignKey('emission_reports.emission_report_pk'))
)

class CSRDReport(Base):
    """
    A CSRD (Corporate Sustainability Reporting Directive) compliant report.
    """
    __tablename__ = "csrd_reports"

    csrd_report_pk = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    reporting_period_start = Column(DateTime, nullable=False)
    reporting_period_end = Column(DateTime, nullable=False)
    organization_id = Column(String, ForeignKey("organizations.organization_pk"), nullable=False)
    report_type = Column(Enum(CSRDReportType), nullable=False)
    status = Column(Enum(CSRDReportStatus), nullable=False)
    version = Column(String, nullable=False)
    prepared_by = Column(String, nullable=False)
    approved_by = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    # Relationships
    organization = relationship("Organization", back_populates="csrd_reports")
    emission_reports = relationship("EmissionReport", secondary=csrd_emission_reports, back_populates="csrd_reports")
    
    # Additional CSRD-specific fields
    esrs_compliance = Column(JSON, nullable=True, comment="Compliance status with European Sustainability Reporting Standards")
    materiality_assessment = Column(JSON, nullable=True, comment="Results of materiality assessment")
    double_materiality = Column(JSON, nullable=True, comment="Double materiality analysis results")
    sustainability_targets = Column(JSON, nullable=True, comment="Sustainability targets and progress")
    value_chain_assessment = Column(JSON, nullable=True, comment="Value chain sustainability assessment")
