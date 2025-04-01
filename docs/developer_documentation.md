# OpenFootprint Developer Documentation

## Architecture Overview

OpenFootprint is built using a modern, scalable architecture designed to support CSRD compliance reporting requirements. The application follows a three-tier architecture:

1. **Presentation Layer**: React-based frontend
2. **Application Layer**: FastAPI backend services
3. **Data Layer**: PostgreSQL database

### System Components

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │     │                 │
│  React Frontend │────▶│  FastAPI Backend│────▶│  PostgreSQL DB  │
│                 │     │                 │     │                 │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## Technology Stack

### Backend
- **Framework**: FastAPI
- **Language**: Python 3.10+
- **ORM**: SQLAlchemy
- **Database**: PostgreSQL
- **API Documentation**: Swagger/OpenAPI
- **Authentication**: JWT-based authentication
- **Validation**: Pydantic

### Frontend
- **Framework**: React
- **State Management**: React Hooks
- **Routing**: React Router
- **Styling**: CSS with component-based styling
- **HTTP Client**: Fetch API

## Project Structure

```
openfootprint/
├── backend/
│   ├── alembic/              # Database migrations
│   ├── app/
│   │   ├── api/              # API endpoints
│   │   ├── db/               # Database models and connection
│   │   ├── models/           # Pydantic models for API validation
│   │   ├── services/         # Business logic
│   │   └── main.py           # Application entry point
│   ├── tests/                # Backend tests
│   └── requirements.txt      # Python dependencies
├── frontend/
│   ├── public/               # Static assets
│   ├── src/
│   │   ├── pages/            # React page components
│   │   ├── components/       # Reusable React components
│   │   ├── services/         # API client services
│   │   ├── utils/            # Utility functions
│   │   ├── App.js            # Main application component
│   │   └── index.js          # Entry point
│   ├── tests/                # Frontend tests
│   └── package.json          # Node.js dependencies
├── docs/                     # Documentation
└── scripts/                  # Utility scripts
```

## Data Model

The OpenFootprint data model is designed to support CSRD compliance reporting requirements. The core entities include:

### Organization
Represents a company or organizational unit.

### Facility
Represents a physical location owned or operated by an organization.

### EmissionReport
Represents a collection of emission data for a specific reporting period.

### EmissionStatement
Represents individual emission data points.

### CSRDReport
Represents a CSRD-compliant report that includes emission data and additional sustainability information.

## Backend Development

### Setting Up Development Environment

1. Clone the repository:
   ```bash
   git clone https://github.com/d-ajvdvoort/openfootprint.git
   cd openfootprint
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   # Create a PostgreSQL database
   # Update database connection string in app/db/database.py
   
   # Run migrations
   alembic upgrade head
   ```

5. Run the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

### Adding a New API Endpoint

1. Create a new file in the `app/api` directory or add to an existing one.
2. Define the endpoint using FastAPI decorators:
   ```python
   from fastapi import APIRouter, Depends, HTTPException
   from sqlalchemy.orm import Session
   
   from app.db.database import get_db
   from app.models.your_model import YourModel, YourModelCreate
   from app.services import your_service
   
   router = APIRouter(
       prefix="/api/your-endpoint",
       tags=["your-tag"],
   )
   
   @router.get("/", response_model=list[YourModel])
   async def get_items(db: Session = Depends(get_db)):
       return your_service.get_items(db)
   
   @router.post("/", response_model=YourModel)
   async def create_item(item: YourModelCreate, db: Session = Depends(get_db)):
       return your_service.create_item(db, item)
   ```

3. Include the router in `app/main.py`:
   ```python
   from app.api import your_endpoint
   
   app.include_router(your_endpoint.router)
   ```

### Adding a New Model

1. Create a Pydantic model in `app/models`:
   ```python
   from pydantic import BaseModel, Field
   from typing import Optional
   
   class YourModelBase(BaseModel):
       name: str
       description: Optional[str] = None
   
   class YourModelCreate(YourModelBase):
       your_model_pk: str
   
   class YourModel(YourModelBase):
       your_model_pk: str
       
       class Config:
           orm_mode = True
   ```

2. Create a SQLAlchemy model in `app/db/models.py`:
   ```python
   from sqlalchemy import Column, String
   from app.db.database import Base
   
   class YourModel(Base):
       __tablename__ = "your_models"
       
       your_model_pk = Column(String, primary_key=True)
       name = Column(String, nullable=False)
       description = Column(String, nullable=True)
   ```

3. Create a migration:
   ```bash
   alembic revision --autogenerate -m "Add YourModel table"
   alembic upgrade head
   ```

### Adding a New Service

Create a new file in `app/services`:
```python
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.models import YourModel as DBYourModel
from app.models.your_model import YourModelCreate

def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[DBYourModel]:
    return db.query(DBYourModel).offset(skip).limit(limit).all()

def get_item(db: Session, your_model_pk: str) -> Optional[DBYourModel]:
    return db.query(DBYourModel).filter(DBYourModel.your_model_pk == your_model_pk).first()

def create_item(db: Session, item: YourModelCreate) -> DBYourModel:
    db_item = DBYourModel(
        your_model_pk=item.your_model_pk,
        name=item.name,
        description=item.description
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
```

## Frontend Development

### Setting Up Development Environment

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Run the development server:
   ```bash
   npm start
   ```

### Adding a New Page

1. Create a new file in `src/pages`:
   ```jsx
   import React, { useState, useEffect } from 'react';
   import './YourPage.css';
   
   const YourPage = () => {
     const [data, setData] = useState([]);
     const [loading, setLoading] = useState(true);
     
     useEffect(() => {
       // Fetch data from API
       fetch('/api/your-endpoint')
         .then(response => response.json())
         .then(data => {
           setData(data);
           setLoading(false);
         });
     }, []);
     
     return (
       <div className="your-page">
         <h1>Your Page Title</h1>
         
         {loading ? (
           <div className="loading">Loading data...</div>
         ) : (
           <div className="data-list">
             {data.map(item => (
               <div key={item.your_model_pk} className="data-item">
                 <h2>{item.name}</h2>
                 <p>{item.description}</p>
               </div>
             ))}
           </div>
         )}
       </div>
     );
   };
   
   export default YourPage;
   ```

2. Create a CSS file for styling:
   ```css
   .your-page {
     padding: 20px;
     max-width: 1200px;
     margin: 0 auto;
   }
   
   .your-page h1 {
     color: #333;
     margin-bottom: 30px;
   }
   
   .loading {
     text-align: center;
     padding: 40px;
     font-size: 18px;
     color: #666;
   }
   
   .data-list {
     display: grid;
     grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
     gap: 20px;
   }
   
   .data-item {
     background-color: #fff;
     border-radius: 8px;
     padding: 20px;
     box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
   }
   ```

3. Add the page to the router in `src/App.js`:
   ```jsx
   import YourPage from './pages/YourPage';
   
   // In the Routes component
   <Route path="/your-page" element={<YourPage />} />
   
   // Add to navigation
   <li><Link to="/your-page">Your Page</Link></li>
   ```

## Testing

### Backend Testing

Run backend tests:
```bash
cd backend
pytest
```

### Frontend Testing

Run frontend tests:
```bash
cd frontend
npm test
```

## Deployment

### Backend Deployment

1. Build the backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Run with a production ASGI server:
   ```bash
   gunicorn -k uvicorn.workers.UvicornWorker app.main:app
   ```

### Frontend Deployment

1. Build the frontend:
   ```bash
   cd frontend
   npm run build
   ```

2. Serve the static files with a web server like Nginx.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write tests for your changes
5. Run the test suite to ensure everything passes
6. Submit a pull request

## Code Style Guidelines

### Python
- Follow PEP 8 guidelines
- Use type hints
- Document functions and classes with docstrings

### JavaScript/React
- Use functional components with hooks
- Follow ESLint configuration
- Use descriptive variable and function names

## Troubleshooting

### Common Development Issues

- **Database connection errors**: Check database credentials and ensure PostgreSQL is running
- **API endpoint not found**: Verify the router is properly included in main.py
- **Frontend build errors**: Check for missing dependencies or syntax errors
- **CORS issues**: Ensure CORS middleware is properly configured in the backend

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [React Documentation](https://reactjs.org/docs/getting-started.html)
- [CSRD Documentation](https://finance.ec.europa.eu/capital-markets-union-and-financial-markets/company-reporting-and-auditing/corporate-sustainability-reporting_en)
- [ESRS Documentation](https://www.efrag.org/Activities/2105191406363055/Sustainability-reporting-standards-interim-draft)
