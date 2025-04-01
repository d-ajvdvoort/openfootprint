from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class EmissionStatement(Base):
    __tablename__ = "emission_statements"
    
    emission_statement_pk = Column(String, primary_key=True)
    emission_activity_id = Column(String, nullable=False)
    emission_calculation_model_id = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    
    def __repr__(self):
        return f"<EmissionStatement(pk={self.emission_statement_pk})>"
