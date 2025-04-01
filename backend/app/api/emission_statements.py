from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.models.emission_statement import EmissionStatement
from app.services import emission_service

router = APIRouter(
    prefix="/api/emission-statements",
    tags=["emission-statements"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[EmissionStatement])
async def get_emission_statements(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of emission statements.
    """
    return emission_service.get_emission_statements(db, skip=skip, limit=limit)

@router.get("/{emission_statement_pk}", response_model=EmissionStatement)
async def get_emission_statement(emission_statement_pk: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific emission statement by its primary key.
    """
    db_emission_statement = emission_service.get_emission_statement(db, emission_statement_pk=emission_statement_pk)
    if db_emission_statement is None:
        raise HTTPException(status_code=404, detail="Emission statement not found")
    return db_emission_statement

@router.post("/", response_model=EmissionStatement)
async def create_emission_statement(emission_statement: EmissionStatement, db: Session = Depends(get_db)):
    """
    Create a new emission statement.
    """
    return emission_service.create_emission_statement(db, emission_statement=emission_statement)
