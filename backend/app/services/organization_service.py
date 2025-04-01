from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.models import Organization as DBOrganization
from app.models.organization import OrganizationCreate, Organization

def get_organizations(db: Session, skip: int = 0, limit: int = 100) -> List[DBOrganization]:
    """
    Retrieve a list of organizations from the database.
    """
    return db.query(DBOrganization).offset(skip).limit(limit).all()

def get_organization(db: Session, organization_pk: str) -> Optional[DBOrganization]:
    """
    Retrieve a specific organization by its primary key.
    """
    return db.query(DBOrganization).filter(DBOrganization.organization_pk == organization_pk).first()

def create_organization(db: Session, organization: OrganizationCreate) -> DBOrganization:
    """
    Create a new organization in the database.
    """
    db_organization = DBOrganization(
        organization_pk=organization.organization_pk,
        name=organization.name,
        description=organization.description,
        parent_organization_id=organization.parent_organization_id
    )
    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)
    return db_organization
