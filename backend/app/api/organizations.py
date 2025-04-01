from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.organization import Organization, OrganizationCreate
from app.services import organization_service

router = APIRouter(
    prefix="/api/organizations",
    tags=["organizations"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[Organization])
async def get_organizations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of organizations.
    """
    return organization_service.get_organizations(db, skip=skip, limit=limit)

@router.get("/{organization_pk}", response_model=Organization)
async def get_organization(organization_pk: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific organization by its primary key.
    """
    db_organization = organization_service.get_organization(db, organization_pk=organization_pk)
    if db_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_organization

@router.post("/", response_model=Organization)
async def create_organization(organization: OrganizationCreate, db: Session = Depends(get_db)):
    """
    Create a new organization.
    """
    return organization_service.create_organization(db, organization=organization)
