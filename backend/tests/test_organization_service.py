import unittest
from unittest.mock import MagicMock, patch
import sys
import os
from datetime import datetime

# Add the backend directory to the path so we can import the modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from app.services import organization_service
from app.models.organization import OrganizationCreate

class TestOrganizationService(unittest.TestCase):
    def setUp(self):
        # Create a mock database session
        self.mock_db = MagicMock()
        
        # Sample test data
        self.sample_organization = {
            "organization_pk": "namespace:master-data--Organization:test123",
            "name": "Test Organization",
            "description": "Test description",
            "parent_organization_id": None
        }
        
    def test_create_organization(self):
        # Create an OrganizationCreate instance
        organization_create = OrganizationCreate(**self.sample_organization)
        
        # Call the service method
        result = organization_service.create_organization(self.mock_db, organization_create)
        
        # Assert that the database add and commit methods were called
        self.mock_db.add.assert_called_once()
        self.mock_db.commit.assert_called_once()
        
        # Assert that the result has the expected attributes
        self.assertEqual(result.organization_pk, self.sample_organization["organization_pk"])
        self.assertEqual(result.name, self.sample_organization["name"])
        self.assertEqual(result.description, self.sample_organization["description"])
    
    def test_get_organization(self):
        # Mock the database query
        mock_org = MagicMock()
        mock_org.organization_pk = self.sample_organization["organization_pk"]
        self.mock_db.query.return_value.filter.return_value.first.return_value = mock_org
        
        # Call the service method
        result = organization_service.get_organization(self.mock_db, self.sample_organization["organization_pk"])
        
        # Assert that the result is the mock organization
        self.assertEqual(result, mock_org)
        
    def test_get_organizations(self):
        # Mock the database query
        mock_orgs = [MagicMock(), MagicMock()]
        self.mock_db.query.return_value.offset.return_value.limit.return_value.all.return_value = mock_orgs
        
        # Call the service method
        result = organization_service.get_organizations(self.mock_db, skip=0, limit=100)
        
        # Assert that the result is the list of mock organizations
        self.assertEqual(result, mock_orgs)

if __name__ == '__main__':
    unittest.main()
