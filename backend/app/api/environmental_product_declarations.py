from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.environmental_product_declaration import EnvironmentalProductDeclaration, EnvironmentalProductDeclarationCreate
from app.services import environmental_product_declaration_service

router = APIRouter(
    prefix="/api/environmental-product-declarations",
    tags=["environmental-product-declarations"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[EnvironmentalProductDeclaration])
async def get_environmental_product_declarations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of environmental product declarations.
    """
    return environmental_product_declaration_service.get_environmental_product_declarations(db, skip=skip, limit=limit)

@router.get("/{environmental_product_declaration_pk}", response_model=EnvironmentalProductDeclaration)
async def get_environmental_product_declaration(environmental_product_declaration_pk: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific environmental product declaration by its primary key.
    """
    db_epd = environmental_product_declaration_service.get_environmental_product_declaration(
        db, environmental_product_declaration_pk=environmental_product_declaration_pk
    )
    if db_epd is None:
        raise HTTPException(status_code=404, detail="Environmental product declaration not found")
    return db_epd

@router.post("/", response_model=EnvironmentalProductDeclaration)
async def create_environmental_product_declaration(epd: EnvironmentalProductDeclarationCreate, db: Session = Depends(get_db)):
    """
    Create a new environmental product declaration.
    """
    return environmental_product_declaration_service.create_environmental_product_declaration(db, epd=epd)
