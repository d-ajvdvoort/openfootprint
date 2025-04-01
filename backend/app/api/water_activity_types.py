from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.water_activity_type import WaterActivityType, WaterActivityTypeCreate
from app.services import water_activity_type_service

router = APIRouter(
    prefix="/api/water-activity-types",
    tags=["water-activity-types"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[WaterActivityType])
async def get_water_activity_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of water activity types.
    """
    return water_activity_type_service.get_water_activity_types(db, skip=skip, limit=limit)

@router.get("/{water_activity_type_id}", response_model=WaterActivityType)
async def get_water_activity_type(water_activity_type_id: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific water activity type by its ID.
    """
    db_water_activity_type = water_activity_type_service.get_water_activity_type(db, water_activity_type_id=water_activity_type_id)
    if db_water_activity_type is None:
        raise HTTPException(status_code=404, detail="Water activity type not found")
    return db_water_activity_type

@router.post("/", response_model=WaterActivityType)
async def create_water_activity_type(water_activity_type: WaterActivityTypeCreate, db: Session = Depends(get_db)):
    """
    Create a new water activity type.
    """
    return water_activity_type_service.create_water_activity_type(db, water_activity_type=water_activity_type)
