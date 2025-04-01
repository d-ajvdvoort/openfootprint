from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.models import WaterActivityType as DBWaterActivityType
from app.models.water_activity_type import WaterActivityTypeCreate, WaterActivityType

def get_water_activity_types(db: Session, skip: int = 0, limit: int = 100) -> List[DBWaterActivityType]:
    """
    Retrieve a list of water activity types from the database.
    """
    return db.query(DBWaterActivityType).offset(skip).limit(limit).all()

def get_water_activity_type(db: Session, water_activity_type_id: str) -> Optional[DBWaterActivityType]:
    """
    Retrieve a specific water activity type by its ID.
    """
    return db.query(DBWaterActivityType).filter(DBWaterActivityType.water_activity_type_id == water_activity_type_id).first()

def create_water_activity_type(db: Session, water_activity_type: WaterActivityTypeCreate) -> DBWaterActivityType:
    """
    Create a new water activity type in the database.
    """
    db_water_activity_type = DBWaterActivityType(
        water_activity_type_id=water_activity_type.water_activity_type_id,
        water_activity_type_name=water_activity_type.water_activity_type_name,
        description=water_activity_type.description
    )
    db.add(db_water_activity_type)
    db.commit()
    db.refresh(db_water_activity_type)
    return db_water_activity_type
