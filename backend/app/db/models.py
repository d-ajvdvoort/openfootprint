from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Integer, Float, Boolean, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

Base = declarative_base()

# Association tables for many-to-many relationships
organization_facility = Table(
    'organization_facility',
    Base.metadata,
    Column('organization_id', String, ForeignKey('organizations.organization_pk')),
    Column('facility_id', String, ForeignKey('facilities.facility_pk'))
)

# Core data models based on the JSON files
class EmissionStatement(Base):
    __tablename__ = "emission_statements"
    
    emission_statement_pk = Column(String, primary_key=True)
    emission_activity_id = Column(String, nullable=False)
    emission_calculation_model_id = Column(String, nullable=True)
    value = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    reporting_period_start = Column(DateTime, nullable=False)
    reporting_period_end = Column(DateTime, nullable=False)
    facility_id = Column(String, ForeignKey('facilities.facility_pk'), nullable=True)
    organization_id = Column(String, ForeignKey('organizations.organization_pk'), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    # Relationships
    facility = relationship("Facility", back_populates="emission_statements")
    organization = relationship("Organization", back_populates="emission_statements")
    emission_reports = relationship("EmissionReport", secondary="emission_report_statements", back_populates="emission_statements")
    
    def __repr__(self):
        return f"<EmissionStatement(pk={self.emission_statement_pk})>"

class EmissionReport(Base):
    __tablename__ = "emission_reports"
    
    emission_report_pk = Column(String, primary_key=True)
    description = Column(Text, nullable=True)
    report_period_start = Column(DateTime, nullable=False)
    report_period_end = Column(DateTime, nullable=False)
    organization_id = Column(String, ForeignKey('organizations.organization_pk'), nullable=False)
    report_type = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    # Relationships
    organization = relationship("Organization", back_populates="emission_reports")
    emission_statements = relationship("EmissionStatement", secondary="emission_report_statements", back_populates="emission_reports")
    
    def __repr__(self):
        return f"<EmissionReport(pk={self.emission_report_pk})>"

# Association table for emission reports and statements
emission_report_statements = Table(
    'emission_report_statements',
    Base.metadata,
    Column('emission_report_id', String, ForeignKey('emission_reports.emission_report_pk')),
    Column('emission_statement_id', String, ForeignKey('emission_statements.emission_statement_pk'))
)

class Organization(Base):
    __tablename__ = "organizations"
    
    organization_pk = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    parent_organization_id = Column(String, ForeignKey('organizations.organization_pk'), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    # Relationships
    parent_organization = relationship("Organization", remote_side=[organization_pk])
    facilities = relationship("Facility", secondary=organization_facility, back_populates="organizations")
    emission_statements = relationship("EmissionStatement", back_populates="organization")
    emission_reports = relationship("EmissionReport", back_populates="organization")
    
    def __repr__(self):
        return f"<Organization(pk={self.organization_pk}, name={self.name})>"

class Facility(Base):
    __tablename__ = "facilities"
    
    facility_pk = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    country = Column(String, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    # Relationships
    organizations = relationship("Organization", secondary=organization_facility, back_populates="facilities")
    emission_statements = relationship("EmissionStatement", back_populates="facility")
    
    def __repr__(self):
        return f"<Facility(pk={self.facility_pk}, name={self.name})>"

class EnvironmentalProductDeclaration(Base):
    __tablename__ = "environmental_product_declarations"
    
    environmental_product_declaration_pk = Column(String, primary_key=True)
    description = Column(Text, nullable=True)
    product_name = Column(String, nullable=False)
    organization_id = Column(String, ForeignKey('organizations.organization_pk'), nullable=False)
    valid_from = Column(DateTime, nullable=False)
    valid_to = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    # Relationships
    organization = relationship("Organization")
    
    def __repr__(self):
        return f"<EnvironmentalProductDeclaration(pk={self.environmental_product_declaration_pk})>"

class WaterActivityType(Base):
    __tablename__ = "water_activity_types"
    
    water_activity_type_id = Column(String, primary_key=True)
    water_activity_type_name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    def __repr__(self):
        return f"<WaterActivityType(id={self.water_activity_type_id}, name={self.water_activity_type_name})>"

class DataQuality(Base):
    __tablename__ = "data_quality"
    
    entity_id = Column(String, primary_key=True)
    quality_score = Column(Float, nullable=True)
    verification_status = Column(String, nullable=True)
    verification_date = Column(DateTime, nullable=True)
    verified_by = Column(String, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    def __repr__(self):
        return f"<DataQuality(id={self.entity_id})>"
