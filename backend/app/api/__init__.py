from fastapi import APIRouter, FastAPI
from app.api import organizations, facilities, emission_reports, emission_statements, csrd_reports, excel_export

def include_routers(app: FastAPI):
    """Include all API routers in the FastAPI application"""
    app.include_router(organizations.router)
    app.include_router(facilities.router)
    app.include_router(emission_reports.router)
    app.include_router(emission_statements.router)
    app.include_router(csrd_reports.router)
    app.include_router(excel_export.router)  # Add the Excel export router
