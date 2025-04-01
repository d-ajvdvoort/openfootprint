from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.emission_report import EmissionReport, EmissionReportCreate
from app.services import emission_report_service

router = APIRouter(
    prefix="/api/emission-reports",
    tags=["emission-reports"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[EmissionReport])
async def get_emission_reports(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of emission reports.
    """
    return emission_report_service.get_emission_reports(db, skip=skip, limit=limit)

@router.get("/{emission_report_pk}", response_model=EmissionReport)
async def get_emission_report(emission_report_pk: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific emission report by its primary key.
    """
    db_emission_report = emission_report_service.get_emission_report(db, emission_report_pk=emission_report_pk)
    if db_emission_report is None:
        raise HTTPException(status_code=404, detail="Emission report not found")
    return db_emission_report

@router.post("/", response_model=EmissionReport)
async def create_emission_report(emission_report: EmissionReportCreate, db: Session = Depends(get_db)):
    """
    Create a new emission report.
    """
    return emission_report_service.create_emission_report(db, emission_report=emission_report)
