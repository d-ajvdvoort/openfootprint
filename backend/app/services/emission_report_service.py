from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.models import EmissionReport as DBEmissionReport
from app.models.emission_report import EmissionReportCreate, EmissionReport

def get_emission_reports(db: Session, skip: int = 0, limit: int = 100) -> List[DBEmissionReport]:
    """
    Retrieve a list of emission reports from the database.
    """
    return db.query(DBEmissionReport).offset(skip).limit(limit).all()

def get_emission_report(db: Session, emission_report_pk: str) -> Optional[DBEmissionReport]:
    """
    Retrieve a specific emission report by its primary key.
    """
    return db.query(DBEmissionReport).filter(DBEmissionReport.emission_report_pk == emission_report_pk).first()

def create_emission_report(db: Session, emission_report: EmissionReportCreate) -> DBEmissionReport:
    """
    Create a new emission report in the database.
    """
    db_emission_report = DBEmissionReport(
        emission_report_pk=emission_report.emission_report_pk,
        description=emission_report.description,
        report_period_start=emission_report.report_period_start,
        report_period_end=emission_report.report_period_end,
        organization_id=emission_report.organization_id,
        report_type=emission_report.report_type,
        status=emission_report.status
    )
    db.add(db_emission_report)
    db.commit()
    db.refresh(db_emission_report)
    return db_emission_report
