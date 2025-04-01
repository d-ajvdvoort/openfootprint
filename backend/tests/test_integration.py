import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import json
from datetime import datetime

# Add the backend directory to the path so we can import the modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Import the main FastAPI application
from app.main import app
from fastapi.testclient import TestClient

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        
    def test_api_health_check(self):
        """Test that the API is running and responding to requests."""
        response = self.client.get("/api/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "healthy"})
    
    @patch('app.db.database.get_db')
    def test_csrd_workflow(self, mock_get_db):
        """Test the complete CSRD reporting workflow."""
        # Mock the database session
        mock_db = MagicMock()
        mock_get_db.return_value = mock_db
        
        # 1. Create an organization
        org_data = {
            "organization_pk": "namespace:master-data--Organization:test123",
            "name": "Test Organization",
            "description": "Test description",
            "parent_organization_id": None
        }
        
        # Mock the organization service
        with patch('app.services.organization_service.create_organization') as mock_create_org:
            mock_create_org.return_value = MagicMock(**org_data)
            org_response = self.client.post("/api/organizations/", json=org_data)
            self.assertEqual(org_response.status_code, 200)
        
        # 2. Create a facility
        facility_data = {
            "facility_pk": "namespace:master-data--Facility:test123",
            "name": "Test Facility",
            "description": "Test description",
            "address": "123 Test Street",
            "city": "Test City",
            "country": "Test Country",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
        
        # Mock the facility service
        with patch('app.services.facility_service.create_facility') as mock_create_facility:
            mock_create_facility.return_value = MagicMock(**facility_data)
            facility_response = self.client.post("/api/facilities/", json=facility_data)
            self.assertEqual(facility_response.status_code, 200)
        
        # 3. Create an emission report
        emission_report_data = {
            "emission_report_pk": "namespace:transactional-data--EmissionReport:test123",
            "description": "Test Emission Report",
            "report_period_start": "2024-01-01T00:00:00Z",
            "report_period_end": "2024-12-31T00:00:00Z",
            "organization_id": "namespace:master-data--Organization:test123",
            "report_type": "CSRD",
            "status": "Draft"
        }
        
        # Mock the emission report service
        with patch('app.services.emission_report_service.create_emission_report') as mock_create_report:
            mock_create_report.return_value = MagicMock(**emission_report_data)
            report_response = self.client.post("/api/emission-reports/", json=emission_report_data)
            self.assertEqual(report_response.status_code, 200)
        
        # 4. Create a CSRD report
        csrd_report_data = {
            "csrd_report_pk": "namespace:transactional-data--CSRDReport:test123",
            "title": "Test CSRD Report",
            "description": "Test description",
            "reporting_period_start": "2024-01-01T00:00:00Z",
            "reporting_period_end": "2024-12-31T00:00:00Z",
            "organization_id": "namespace:master-data--Organization:test123",
            "report_type": "Annual",
            "status": "Draft",
            "version": "1.0",
            "prepared_by": "Test User",
            "approved_by": None,
            "emission_report_ids": ["namespace:transactional-data--EmissionReport:test123"]
        }
        
        # Mock the CSRD report service
        with patch('app.services.csrd_report_service.create_csrd_report') as mock_create_csrd:
            mock_create_csrd.return_value = MagicMock(**csrd_report_data)
            csrd_response = self.client.post("/api/csrd-reports/", json=csrd_report_data)
            self.assertEqual(csrd_response.status_code, 200)
        
        # 5. Validate the CSRD report
        validation_data = {
            "overall_status": "passed",
            "validation_date": datetime.now().isoformat(),
            "standards_version": "ESRS 2023",
            "checks": [
                {
                    "standard": "ESRS E1",
                    "description": "Climate change",
                    "status": "passed",
                    "details": "All required climate change disclosures are present"
                }
            ]
        }
        
        # Mock the CSRD report validation service
        with patch('app.services.csrd_report_service.validate_csrd_report') as mock_validate:
            mock_validate.return_value = validation_data
            validate_response = self.client.get(f"/api/csrd-reports/{csrd_report_data['csrd_report_pk']}/validate")
            self.assertEqual(validate_response.status_code, 200)
            self.assertEqual(validate_response.json()["overall_status"], "passed")
        
        # 6. Generate the CSRD report document
        generation_data = {
            "status": "success",
            "message": "CSRD report document generated in pdf format",
            "report_id": csrd_report_data['csrd_report_pk'],
            "generated_at": datetime.now().isoformat(),
            "download_url": f"/api/csrd-reports/{csrd_report_data['csrd_report_pk']}/download?format=pdf"
        }
        
        # Mock the CSRD report generation service
        with patch('app.services.csrd_report_service.generate_report_document') as mock_generate:
            mock_generate.return_value = generation_data
            generate_response = self.client.get(f"/api/csrd-reports/{csrd_report_data['csrd_report_pk']}/generate?format=pdf")
            self.assertEqual(generate_response.status_code, 200)
            self.assertEqual(generate_response.json()["status"], "success")

if __name__ == '__main__':
    unittest.main()
