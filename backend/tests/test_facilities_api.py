import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import json
from datetime import datetime

# Add the backend directory to the path so we can import the modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.api import facilities
from fastapi import HTTPException
from fastapi.testclient import TestClient
from app.main import app

class TestFacilitiesAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        
        # Sample test data
        self.sample_facility = {
            "facility_pk": "namespace:master-data--Facility:test123",
            "name": "Test Facility",
            "description": "Test description",
            "address": "123 Test Street",
            "city": "Test City",
            "country": "Test Country",
            "latitude": 37.7749,
            "longitude": -122.4194
        }
        
    @patch('app.api.facilities.facility_service')
    def test_get_facilities(self, mock_service):
        # Mock the service response
        mock_service.get_facilities.return_value = [MagicMock()]
        
        # Test the API endpoint
        with patch('app.api.facilities.get_db', return_value=MagicMock()):
            response = self.client.get("/api/facilities/")
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called
        mock_service.get_facilities.assert_called_once()
    
    @patch('app.api.facilities.facility_service')
    def test_get_facility(self, mock_service):
        # Mock the service response
        mock_service.get_facility.return_value = MagicMock()
        
        # Test the API endpoint
        with patch('app.api.facilities.get_db', return_value=MagicMock()):
            response = self.client.get(f"/api/facilities/{self.sample_facility['facility_pk']}")
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called with the correct parameters
        mock_service.get_facility.assert_called_once_with(
            MagicMock(), 
            facility_pk=self.sample_facility['facility_pk']
        )
    
    @patch('app.api.facilities.facility_service')
    def test_get_facility_not_found(self, mock_service):
        # Mock the service response
        mock_service.get_facility.return_value = None
        
        # Test the API endpoint
        with patch('app.api.facilities.get_db', return_value=MagicMock()):
            # This should raise an HTTPException with status code 404
            with self.assertRaises(HTTPException) as context:
                facilities.get_facility(
                    self.sample_facility['facility_pk'],
                    MagicMock()
                )
            
            # Assert that the exception has the correct status code
            self.assertEqual(context.exception.status_code, 404)
    
    @patch('app.api.facilities.facility_service')
    def test_create_facility(self, mock_service):
        # Mock the service response
        mock_service.create_facility.return_value = MagicMock()
        
        # Test the API endpoint
        with patch('app.api.facilities.get_db', return_value=MagicMock()):
            response = self.client.post(
                "/api/facilities/",
                json=self.sample_facility
            )
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called
        mock_service.create_facility.assert_called_once()

if __name__ == '__main__':
    unittest.main()
