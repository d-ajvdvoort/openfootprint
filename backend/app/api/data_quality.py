from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.data_quality import DataQuality, DataQualityCreate
from app.services import data_quality_service

router = APIRouter(
    prefix="/api/data-quality",
    tags=["data-quality"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[DataQuality])
async def get_data_quality_entries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of data quality entries.
    """
    return data_quality_service.get_data_quality_entries(db, skip=skip, limit=limit)

@router.get("/{entity_id}", response_model=DataQuality)
async def get_data_quality(entity_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific data quality entry by its entity ID.
    """
    db_data_quality = data_quality_service.get_data_quality(db, entity_id=entity_id)
    if db_data_quality is None:
        raise HTTPException(status_code=404, detail="Data quality entry not found")
    return db_data_quality

@router.post("/", response_model=DataQuality)
async def create_data_quality(data_quality: DataQualityCreate, db: Session = Depends(get_db)):
    """
    Create a new data quality entry.
    """
    return data_quality_service.create_data_quality(db, data_quality=data_quality)
