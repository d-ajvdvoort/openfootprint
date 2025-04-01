from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.models import Facility as DBFacility
from app.models.facility import FacilityCreate, Facility

class FacilityService:
    def get_facilities(self, db: Session, skip: int = 0, limit: int = 100) -> List[DBFacility]:
        """
        Retrieve a list of facilities from the database.
        """
        return db.query(DBFacility).offset(skip).limit(limit).all()

    def get_facility(self, db: Session, facility_pk: str) -> Optional[DBFacility]:
        """
        Retrieve a specific facility by its primary key.
        """
        return db.query(DBFacility).filter(DBFacility.facility_pk == facility_pk).first()

    def create_facility(self, db: Session, facility: FacilityCreate) -> DBFacility:
        """
        Create a new facility in the database.
        """
        db_facility = DBFacility(
            facility_pk=facility.facility_pk,
            name=facility.name,
            description=facility.description,
            address=facility.address,
            city=facility.city,
            country=facility.country,
            latitude=facility.latitude,
            longitude=facility.longitude
        )
        db.add(db_facility)
        db.commit()
        db.refresh(db_facility)
        return db_facility

# For backward compatibility, keep the function versions
def get_facilities(db: Session, skip: int = 0, limit: int = 100) -> List[DBFacility]:
    """
    Retrieve a list of facilities from the database.
    """
    return FacilityService().get_facilities(db, skip, limit)

def get_facility(db: Session, facility_pk: str) -> Optional[DBFacility]:
    """
    Retrieve a specific facility by its primary key.
    """
    return FacilityService().get_facility(db, facility_pk)

def create_facility(db: Session, facility: FacilityCreate) -> DBFacility:
    """
    Create a new facility in the database.
    """
    return FacilityService().create_facility(db, facility)
