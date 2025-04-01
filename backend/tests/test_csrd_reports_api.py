import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import json
from datetime import datetime

# Add the backend directory to the path so we can import the modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.api import csrd_reports
from fastapi import HTTPException
from fastapi.testclient import TestClient
from app.main import app

class TestCSRDReportsAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        
        # Sample test data
        self.sample_csrd_report = {
            "csrd_report_pk": "namespace:transactional-data--CSRDReport:test123",
            "title": "Test CSRD Report",
            "description": "Test description",
            "reporting_period_start": "2024-01-01T00:00:00Z",
            "reporting_period_end": "2024-12-31T00:00:00Z",
            "organization_id": "namespace:master-data--Organization:test456",
            "report_type": "Annual",
            "status": "Draft",
            "version": "1.0",
            "prepared_by": "Test User",
            "approved_by": None,
            "emission_report_ids": ["namespace:transactional-data--EmissionReport:test789"]
        }
        
    @patch('app.api.csrd_reports.csrd_report_service')
    def test_get_csrd_reports(self, mock_service):
        # Mock the service response
        mock_service.get_csrd_reports.return_value = [MagicMock()]
        
        # Test the API endpoint
        with patch('app.api.csrd_reports.get_db', return_value=MagicMock()):
            response = self.client.get("/api/csrd-reports/")
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called
        mock_service.get_csrd_reports.assert_called_once()
    
    @patch('app.api.csrd_reports.csrd_report_service')
    def test_get_csrd_report(self, mock_service):
        # Mock the service response
        mock_service.get_csrd_report.return_value = MagicMock()
        
        # Test the API endpoint
        with patch('app.api.csrd_reports.get_db', return_value=MagicMock()):
            response = self.client.get(f"/api/csrd-reports/{self.sample_csrd_report['csrd_report_pk']}")
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called with the correct parameters
        mock_service.get_csrd_report.assert_called_once_with(
            MagicMock(), 
            csrd_report_pk=self.sample_csrd_report['csrd_report_pk']
        )
    
    @patch('app.api.csrd_reports.csrd_report_service')
    def test_get_csrd_report_not_found(self, mock_service):
        # Mock the service response
        mock_service.get_csrd_report.return_value = None
        
        # Test the API endpoint
        with patch('app.api.csrd_reports.get_db', return_value=MagicMock()):
            # This should raise an HTTPException with status code 404
            with self.assertRaises(HTTPException) as context:
                csrd_reports.get_csrd_report(
                    self.sample_csrd_report['csrd_report_pk'],
                    MagicMock()
                )
            
            # Assert that the exception has the correct status code
            self.assertEqual(context.exception.status_code, 404)
    
    @patch('app.api.csrd_reports.csrd_report_service')
    def test_create_csrd_report(self, mock_service):
        # Mock the service response
        mock_service.create_csrd_report.return_value = MagicMock()
        
        # Test the API endpoint
        with patch('app.api.csrd_reports.get_db', return_value=MagicMock()):
            response = self.client.post(
                "/api/csrd-reports/",
                json=self.sample_csrd_report
            )
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called
        mock_service.create_csrd_report.assert_called_once()
    
    @patch('app.api.csrd_reports.csrd_report_service')
    def test_generate_csrd_report_document(self, mock_service):
        # Mock the service response
        mock_service.generate_report_document.return_value = {
            "status": "success",
            "message": "CSRD report document generated in pdf format",
            "report_id": self.sample_csrd_report['csrd_report_pk'],
            "generated_at": datetime.now().isoformat(),
            "download_url": f"/api/csrd-reports/{self.sample_csrd_report['csrd_report_pk']}/download?format=pdf"
        }
        
        # Test the API endpoint
        with patch('app.api.csrd_reports.get_db', return_value=MagicMock()):
            response = self.client.get(
                f"/api/csrd-reports/{self.sample_csrd_report['csrd_report_pk']}/generate?format=pdf"
            )
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called with the correct parameters
        mock_service.generate_report_document.assert_called_once_with(
            MagicMock(), 
            csrd_report_pk=self.sample_csrd_report['csrd_report_pk'],
            format="pdf"
        )
    
    @patch('app.api.csrd_reports.csrd_report_service')
    def test_validate_csrd_report(self, mock_service):
        # Mock the service response
        mock_service.validate_csrd_report.return_value = {
            "overall_status": "passed",
            "validation_date": datetime.now().isoformat(),
            "standards_version": "ESRS 2023",
            "checks": []
        }
        
        # Test the API endpoint
        with patch('app.api.csrd_reports.get_db', return_value=MagicMock()):
            response = self.client.get(
                f"/api/csrd-reports/{self.sample_csrd_report['csrd_report_pk']}/validate"
            )
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called with the correct parameters
        mock_service.validate_csrd_report.assert_called_once_with(
            MagicMock(), 
            csrd_report_pk=self.sample_csrd_report['csrd_report_pk']
        )

if __name__ == '__main__':
    unittest.main()
