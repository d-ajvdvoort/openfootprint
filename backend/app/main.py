from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.api import organizations, facilities, emission_reports, emission_statements, csrd_reports, excel_export

app = FastAPI(
    title="OpenFootprint API",
    description="API for CSRD compliance reporting",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include all API routers
app.include_router(organizations.router)
app.include_router(facilities.router)
app.include_router(emission_reports.router)
app.include_router(emission_statements.router)
app.include_router(csrd_reports.router)
app.include_router(excel_export.router)

@app.get("/")
async def root():
    return {"message": "Welcome to OpenFootprint API for CSRD compliance reporting"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
