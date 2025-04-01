import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import json
from datetime import datetime

# Add the backend directory to the path so we can import the modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.api import emission_reports
from fastapi import HTTPException
from fastapi.testclient import TestClient
from app.main import app

class TestEmissionReportsAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        
        # Sample test data
        self.sample_emission_report = {
            "emission_report_pk": "namespace:transactional-data--EmissionReport:test123",
            "description": "Test Emission Report",
            "report_period_start": "2024-01-01T00:00:00Z",
            "report_period_end": "2024-12-31T00:00:00Z",
            "organization_id": "namespace:master-data--Organization:test456",
            "report_type": "CSRD",
            "status": "Draft"
        }
        
    @patch('app.api.emission_reports.emission_report_service')
    def test_get_emission_reports(self, mock_service):
        # Mock the service response
        mock_service.get_emission_reports.return_value = [MagicMock()]
        
        # Test the API endpoint
        with patch('app.api.emission_reports.get_db', return_value=MagicMock()):
            response = self.client.get("/api/emission-reports/")
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called
        mock_service.get_emission_reports.assert_called_once()
    
    @patch('app.api.emission_reports.emission_report_service')
    def test_get_emission_report(self, mock_service):
        # Mock the service response
        mock_service.get_emission_report.return_value = MagicMock()
        
        # Test the API endpoint
        with patch('app.api.emission_reports.get_db', return_value=MagicMock()):
            response = self.client.get(f"/api/emission-reports/{self.sample_emission_report['emission_report_pk']}")
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called with the correct parameters
        mock_service.get_emission_report.assert_called_once_with(
            MagicMock(), 
            emission_report_pk=self.sample_emission_report['emission_report_pk']
        )
    
    @patch('app.api.emission_reports.emission_report_service')
    def test_get_emission_report_not_found(self, mock_service):
        # Mock the service response
        mock_service.get_emission_report.return_value = None
        
        # Test the API endpoint
        with patch('app.api.emission_reports.get_db', return_value=MagicMock()):
            # This should raise an HTTPException with status code 404
            with self.assertRaises(HTTPException) as context:
                emission_reports.get_emission_report(
                    self.sample_emission_report['emission_report_pk'],
                    MagicMock()
                )
            
            # Assert that the exception has the correct status code
            self.assertEqual(context.exception.status_code, 404)
    
    @patch('app.api.emission_reports.emission_report_service')
    def test_create_emission_report(self, mock_service):
        # Mock the service response
        mock_service.create_emission_report.return_value = MagicMock()
        
        # Test the API endpoint
        with patch('app.api.emission_reports.get_db', return_value=MagicMock()):
            response = self.client.post(
                "/api/emission-reports/",
                json=self.sample_emission_report
            )
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called
        mock_service.create_emission_report.assert_called_once()

if __name__ == '__main__':
    unittest.main()
