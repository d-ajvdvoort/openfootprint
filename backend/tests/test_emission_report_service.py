import unittest
from unittest.mock import MagicMock, patch
import sys
import os
from datetime import datetime

# Add the backend directory to the path so we can import the modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.services import emission_report_service
from app.models.emission_report import EmissionReportCreate

class TestEmissionReportService(unittest.TestCase):
    def setUp(self):
        # Create a mock database session
        self.mock_db = MagicMock()
        
        # Sample test data
        self.sample_emission_report = {
            "emission_report_pk": "namespace:transactional-data--EmissionReport:test123",
            "description": "Test Emission Report",
            "report_period_start": datetime(2024, 1, 1),
            "report_period_end": datetime(2024, 12, 31),
            "organization_id": "namespace:master-data--Organization:test456",
            "report_type": "CSRD",
            "status": "Draft"
        }
        
    def test_create_emission_report(self):
        # Create an EmissionReportCreate instance
        emission_report_create = EmissionReportCreate(**self.sample_emission_report)
        
        # Call the service method
        result = emission_report_service.create_emission_report(self.mock_db, emission_report_create)
        
        # Assert that the database add and commit methods were called
        self.mock_db.add.assert_called_once()
        self.mock_db.commit.assert_called_once()
        
        # Assert that the result has the expected attributes
        self.assertEqual(result.emission_report_pk, self.sample_emission_report["emission_report_pk"])
        self.assertEqual(result.description, self.sample_emission_report["description"])
        self.assertEqual(result.report_period_start, self.sample_emission_report["report_period_start"])
        self.assertEqual(result.report_period_end, self.sample_emission_report["report_period_end"])
        self.assertEqual(result.organization_id, self.sample_emission_report["organization_id"])
        self.assertEqual(result.report_type, self.sample_emission_report["report_type"])
        self.assertEqual(result.status, self.sample_emission_report["status"])
    
    def test_get_emission_report(self):
        # Mock the database query
        mock_report = MagicMock()
        mock_report.emission_report_pk = self.sample_emission_report["emission_report_pk"]
        self.mock_db.query.return_value.filter.return_value.first.return_value = mock_report
        
        # Call the service method
        result = emission_report_service.get_emission_report(self.mock_db, self.sample_emission_report["emission_report_pk"])
        
        # Assert that the result is the mock report
        self.assertEqual(result, mock_report)
        
    def test_get_emission_reports(self):
        # Mock the database query
        mock_reports = [MagicMock(), MagicMock()]
        self.mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = mock_reports
        
        # Call the service method
        result = emission_report_service.get_emission_reports(self.mock_db, skip=0, limit=100)
        
        # Assert that the result is the list of mock reports
        self.assertEqual(result, mock_reports)

if __name__ == '__main__':
    unittest.main()
