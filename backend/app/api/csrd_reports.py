from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.csrd_report import CSRDReport, CSRDReportCreate
from app.services import csrd_report_service

router = APIRouter(
    prefix="/api/csrd-reports",
    tags=["csrd-reports"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[CSRDReport])
async def get_csrd_reports(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of CSRD reports.
    """
    return csrd_report_service.get_csrd_reports(db, skip=skip, limit=limit)

@router.get("/{csrd_report_pk}", response_model=CSRDReport)
async def get_csrd_report(csrd_report_pk: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific CSRD report by its primary key.
    """
    db_csrd_report = csrd_report_service.get_csrd_report(db, csrd_report_pk=csrd_report_pk)
    if db_csrd_report is None:
        raise HTTPException(status_code=404, detail="CSRD report not found")
    return db_csrd_report

@router.post("/", response_model=CSRDReport)
async def create_csrd_report(csrd_report: CSRDReportCreate, db: Session = Depends(get_db)):
    """
    Create a new CSRD report.
    """
    return csrd_report_service.create_csrd_report(db, csrd_report=csrd_report)

@router.get("/{csrd_report_pk}/generate", response_model=dict)
async def generate_csrd_report_document(csrd_report_pk: str, format: str = "pdf", db: Session = Depends(get_db)):
    """
    Generate a CSRD-compliant report document in the specified format.
    """
    return csrd_report_service.generate_report_document(db, csrd_report_pk=csrd_report_pk, format=format)

@router.get("/{csrd_report_pk}/validate", response_model=dict)
async def validate_csrd_report(csrd_report_pk: str, db: Session = Depends(get_db)):
    """
    Validate a CSRD report against ESRS requirements.
    """
    return csrd_report_service.validate_csrd_report(db, csrd_report_pk=csrd_report_pk)
