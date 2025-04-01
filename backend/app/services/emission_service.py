from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.models import EmissionStatement as DBEmissionStatement
from app.models.emission_statement import EmissionStatement

def get_emission_statements(db: Session, skip: int = 0, limit: int = 100) -> List[DBEmissionStatement]:
    """
    Retrieve a list of emission statements from the database.
    """
    return db.query(DBEmissionStatement).offset(skip).limit(limit).all()

def get_emission_statement(db: Session, emission_statement_pk: str) -> Optional[DBEmissionStatement]:
    """
    Retrieve a specific emission statement by its primary key.
    """
    return db.query(DBEmissionStatement).filter(DBEmissionStatement.emission_statement_pk == emission_statement_pk).first()

def create_emission_statement(db: Session, emission_statement: EmissionStatement) -> DBEmissionStatement:
    """
    Create a new emission statement in the database.
    """
    db_emission_statement = DBEmissionStatement(
        emission_statement_pk=emission_statement.emission_statement_pk,
        emission_activity_id=emission_statement.emission_activity_id,
        emission_calculation_model_id=emission_statement.emission_calculation_model_id
    )
    db.add(db_emission_statement)
    db.commit()
    db.refresh(db_emission_statement)
    return db_emission_statement
