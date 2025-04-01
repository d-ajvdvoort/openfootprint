from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.models import DataQuality as DBDataQuality
from app.models.data_quality import DataQualityCreate, DataQuality

def get_data_quality_entries(db: Session, skip: int = 0, limit: int = 100) -> List[DBDataQuality]:
    """
    Retrieve a list of data quality entries from the database.
    """
    return db.query(DBDataQuality).offset(skip).limit(limit).all()

def get_data_quality(db: Session, entity_id: str) -> Optional[DBDataQuality]:
    """
    Retrieve a specific data quality entry by its entity ID.
    """
    return db.query(DBDataQuality).filter(DBDataQuality.entity_id == entity_id).first()

def create_data_quality(db: Session, data_quality: DataQualityCreate) -> DBDataQuality:
    """
    Create a new data quality entry in the database.
    """
    db_data_quality = DBDataQuality(
        entity_id=data_quality.entity_id,
        quality_score=data_quality.quality_score,
        verification_status=data_quality.verification_status,
        verification_date=data_quality.verification_date,
        verified_by=data_quality.verified_by,
        notes=data_quality.notes
    )
    db.add(db_data_quality)
    db.commit()
    db.refresh(db_data_quality)
    return db_data_quality
