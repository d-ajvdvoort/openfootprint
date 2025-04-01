from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.facility import Facility, FacilityCreate
from app.services import facility_service

router = APIRouter(
    prefix="/api/facilities",
    tags=["facilities"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[Facility])
async def get_facilities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of facilities.
    """
    return facility_service.get_facilities(db, skip=skip, limit=limit)

@router.get("/{facility_pk}", response_model=Facility)
async def get_facility(facility_pk: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific facility by its primary key.
    """
    db_facility = facility_service.get_facility(db, facility_pk=facility_pk)
    if db_facility is None:
        raise HTTPException(status_code=404, detail="Facility not found")
    return db_facility

@router.post("/", response_model=Facility)
async def create_facility(facility: FacilityCreate, db: Session = Depends(get_db)):
    """
    Create a new facility.
    """
    return facility_service.create_facility(db, facility=facility)
