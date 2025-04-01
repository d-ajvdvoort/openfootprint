from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.models import EnvironmentalProductDeclaration as DBEnvironmentalProductDeclaration
from app.models.environmental_product_declaration import EnvironmentalProductDeclarationCreate, EnvironmentalProductDeclaration

def get_environmental_product_declarations(db: Session, skip: int = 0, limit: int = 100) -> List[DBEnvironmentalProductDeclaration]:
    """
    Retrieve a list of environmental product declarations from the database.
    """
    return db.query(DBEnvironmentalProductDeclaration).offset(skip).limit(limit).all()

def get_environmental_product_declaration(db: Session, environmental_product_declaration_pk: str) -> Optional[DBEnvironmentalProductDeclaration]:
    """
    Retrieve a specific environmental product declaration by its primary key.
    """
    return db.query(DBEnvironmentalProductDeclaration).filter(
        DBEnvironmentalProductDeclaration.environmental_product_declaration_pk == environmental_product_declaration_pk
    ).first()

def create_environmental_product_declaration(db: Session, epd: EnvironmentalProductDeclarationCreate) -> DBEnvironmentalProductDeclaration:
    """
    Create a new environmental product declaration in the database.
    """
    db_epd = DBEnvironmentalProductDeclaration(
        environmental_product_declaration_pk=epd.environmental_product_declaration_pk,
        description=epd.description,
        product_name=epd.product_name,
        organization_id=epd.organization_id,
        valid_from=epd.valid_from,
        valid_to=epd.valid_to
    )
    db.add(db_epd)
    db.commit()
    db.refresh(db_epd)
    return db_epd
