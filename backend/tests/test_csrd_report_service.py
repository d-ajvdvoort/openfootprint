import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import json
from datetime import datetime

# Add the backend directory to the path so we can import the modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.services import csrd_report_service
from app.models.csrd_report import CSRDReportCreate, CSRDReport

class TestCSRDReportService(unittest.TestCase):
    def setUp(self):
        # Create a mock database session
        self.mock_db = MagicMock()
        
        # Sample test data
        self.sample_csrd_report = {
            "csrd_report_pk": "namespace:transactional-data--CSRDReport:test123",
            "title": "Test CSRD Report",
            "description": "Test description",
            "reporting_period_start": datetime(2024, 1, 1),
            "reporting_period_end": datetime(2024, 12, 31),
            "organization_id": "namespace:master-data--Organization:test456",
            "report_type": "Annual",
            "status": "Draft",
            "version": "1.0",
            "prepared_by": "Test User",
            "approved_by": None,
            "emission_report_ids": ["namespace:transactional-data--EmissionReport:test789"]
        }
        
    def test_create_csrd_report(self):
        # Create a CSRDReportCreate instance
        csrd_report_create = CSRDReportCreate(**self.sample_csrd_report)
        
        # Mock the database query and add methods
        self.mock_db.query.return_value.filter.return_value.first.return_value = MagicMock()
        
        # Call the service method
        with patch('app.db.models.EmissionReport'):
            result = csrd_report_service.create_csrd_report(self.mock_db, csrd_report_create)
        
        # Assert that the database add and commit methods were called
        self.mock_db.add.assert_called_once()
        self.mock_db.commit.assert_called()
        
        # Assert that the result has the expected attributes
        self.assertEqual(result.csrd_report_pk, self.sample_csrd_report["csrd_report_pk"])
        self.assertEqual(result.title, self.sample_csrd_report["title"])
        self.assertEqual(result.organization_id, self.sample_csrd_report["organization_id"])
    
    def test_get_csrd_report(self):
        # Mock the database query
        mock_report = MagicMock()
        mock_report.csrd_report_pk = self.sample_csrd_report["csrd_report_pk"]
        self.mock_db.query.return_value.filter.return_value.first.return_value = mock_report
        
        # Call the service method
        result = csrd_report_service.get_csrd_report(self.mock_db, self.sample_csrd_report["csrd_report_pk"])
        
        # Assert that the result is the mock report
        self.assertEqual(result, mock_report)
        
    def test_generate_report_document(self):
        # Mock the get_csrd_report method
        mock_report = MagicMock()
        with patch('app.services.csrd_report_service.get_csrd_report', return_value=mock_report):
            result = csrd_report_service.generate_report_document(self.mock_db, self.sample_csrd_report["csrd_report_pk"], "pdf")
        
        # Assert that the result has the expected keys
        self.assertIn("status", result)
        self.assertIn("message", result)
        self.assertIn("report_id", result)
        self.assertIn("generated_at", result)
        self.assertIn("download_url", result)
        
    def test_validate_csrd_report(self):
        # Mock the get_csrd_report method
        mock_report = MagicMock()
        with patch('app.services.csrd_report_service.get_csrd_report', return_value=mock_report):
            result = csrd_report_service.validate_csrd_report(self.mock_db, self.sample_csrd_report["csrd_report_pk"])
        
        # Assert that the result has the expected keys
        self.assertIn("overall_status", result)
        self.assertIn("validation_date", result)
        self.assertIn("standards_version", result)
        self.assertIn("checks", result)
        
        # Assert that the database commit method was called
        self.mock_db.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
