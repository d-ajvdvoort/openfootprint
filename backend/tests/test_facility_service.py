import unittest
from unittest.mock import MagicMock, patch
import sys
import os
from datetime import datetime

# Add the backend directory to the path so we can import the modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.services import facility_service
from app.models.facility import FacilityCreate

class TestFacilityService(unittest.TestCase):
    def setUp(self):
        # Create a mock database session
        self.mock_db = MagicMock()
        
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
        
    def test_create_facility(self):
        # Create a FacilityCreate instance
        facility_create = FacilityCreate(**self.sample_facility)
        
        # Call the service method
        result = facility_service.create_facility(self.mock_db, facility_create)
        
        # Assert that the database add and commit methods were called
        self.mock_db.add.assert_called_once()
        self.mock_db.commit.assert_called_once()
        
        # Assert that the result has the expected attributes
        self.assertEqual(result.facility_pk, self.sample_facility["facility_pk"])
        self.assertEqual(result.name, self.sample_facility["name"])
        self.assertEqual(result.description, self.sample_facility["description"])
        self.assertEqual(result.address, self.sample_facility["address"])
        self.assertEqual(result.city, self.sample_facility["city"])
        self.assertEqual(result.country, self.sample_facility["country"])
        self.assertEqual(result.latitude, self.sample_facility["latitude"])
        self.assertEqual(result.longitude, self.sample_facility["longitude"])
    
    def test_get_facility(self):
        # Mock the database query
        mock_facility = MagicMock()
        mock_facility.facility_pk = self.sample_facility["facility_pk"]
        self.mock_db.query.return_value.filter.return_value.first.return_value = mock_facility
        
        # Call the service method
        result = facility_service.get_facility(self.mock_db, self.sample_facility["facility_pk"])
        
        # Assert that the result is the mock facility
        self.assertEqual(result, mock_facility)
        
    def test_get_facilities(self):
        # Mock the database query
        mock_facilities = [MagicMock(), MagicMock()]
        self.mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = mock_facilities
        
        # Call the service method
        result = facility_service.get_facilities(self.mock_db, skip=0, limit=100)
        
        # Assert that the result is the list of mock facilities
        self.assertEqual(result, mock_facilities)

if __name__ == '__main__':
    unittest.main()
