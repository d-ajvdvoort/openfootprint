import unittest
from unittest.mock import MagicMock, patch
import sys
import os
import json
from datetime import datetime

# Add the backend directory to the path so we can import the modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.api import organizations
from fastapi import HTTPException
from fastapi.testclient import TestClient
from app.main import app

class TestOrganizationsAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        
        # Sample test data
        self.sample_organization = {
            "organization_pk": "namespace:master-data--Organization:test123",
            "name": "Test Organization",
            "description": "Test description",
            "parent_organization_id": None
        }
        
    @patch('app.api.organizations.organization_service')
    def test_get_organizations(self, mock_service):
        # Mock the service response
        mock_service.get_organizations.return_value = [MagicMock()]
        
        # Test the API endpoint
        with patch('app.api.organizations.get_db', return_value=MagicMock()):
            response = self.client.get("/api/organizations/")
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called
        mock_service.get_organizations.assert_called_once()
    
    @patch('app.api.organizations.organization_service')
    def test_get_organization(self, mock_service):
        # Mock the service response
        mock_service.get_organization.return_value = MagicMock()
        
        # Test the API endpoint
        with patch('app.api.organizations.get_db', return_value=MagicMock()):
            response = self.client.get(f"/api/organizations/{self.sample_organization['organization_pk']}")
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called with the correct parameters
        mock_service.get_organization.assert_called_once_with(
            MagicMock(), 
            organization_pk=self.sample_organization['organization_pk']
        )
    
    @patch('app.api.organizations.organization_service')
    def test_get_organization_not_found(self, mock_service):
        # Mock the service response
        mock_service.get_organization.return_value = None
        
        # Test the API endpoint
        with patch('app.api.organizations.get_db', return_value=MagicMock()):
            # This should raise an HTTPException with status code 404
            with self.assertRaises(HTTPException) as context:
                organizations.get_organization(
                    self.sample_organization['organization_pk'],
                    MagicMock()
                )
            
            # Assert that the exception has the correct status code
            self.assertEqual(context.exception.status_code, 404)
    
    @patch('app.api.organizations.organization_service')
    def test_create_organization(self, mock_service):
        # Mock the service response
        mock_service.create_organization.return_value = MagicMock()
        
        # Test the API endpoint
        with patch('app.api.organizations.get_db', return_value=MagicMock()):
            response = self.client.post(
                "/api/organizations/",
                json=self.sample_organization
            )
        
        # Assert that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Assert that the service method was called
        mock_service.create_organization.assert_called_once()

if __name__ == '__main__':
    unittest.main()
