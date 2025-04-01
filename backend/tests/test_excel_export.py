import pytest
from fastapi.testclient import TestClient
from app.main import app
import io
import pandas as pd

client = TestClient(app)

def test_export_organizations_excel():
    """Test the organizations Excel export endpoint"""
    response = client.get("/api/excel/organizations")
    
    # Check response status and headers
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    assert "attachment; filename=organizations.xlsx" in response.headers["Content-Disposition"]
    
    # Verify the Excel content
    excel_data = io.BytesIO(response.content)
    df = pd.read_excel(excel_data)
    
    # Check that the DataFrame has the expected columns
    expected_columns = ["ID", "Name", "Description", "Parent Organization", "Created At", "Updated At"]
    assert all(col in df.columns for col in expected_columns)

def test_export_facilities_excel():
    """Test the facilities Excel export endpoint"""
    response = client.get("/api/excel/facilities")
    
    # Check response status and headers
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    assert "attachment; filename=facilities.xlsx" in response.headers["Content-Disposition"]
    
    # Verify the Excel content
    excel_data = io.BytesIO(response.content)
    df = pd.read_excel(excel_data)
    
    # Check that the DataFrame has the expected columns
    expected_columns = ["ID", "Name", "Description", "Address", "City", "Country", "Latitude", "Longitude", "Created At", "Updated At"]
    assert all(col in df.columns for col in expected_columns)

def test_export_emission_reports_excel():
    """Test the emission reports Excel export endpoint"""
    response = client.get("/api/excel/emission-reports")
    
    # Check response status and headers
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    assert "attachment; filename=emission_reports.xlsx" in response.headers["Content-Disposition"]
    
    # Verify the Excel content
    excel_data = io.BytesIO(response.content)
    df = pd.read_excel(excel_data)
    
    # Check that the DataFrame has the expected columns
    expected_columns = ["ID", "Title", "Description", "Reporting Period", "Status", "Organization ID", "Created At", "Updated At"]
    assert all(col in df.columns for col in expected_columns)

def test_export_csrd_reports_excel():
    """Test the CSRD reports Excel export endpoint"""
    response = client.get("/api/excel/csrd-reports")
    
    # Check response status and headers
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    assert "attachment; filename=csrd_reports.xlsx" in response.headers["Content-Disposition"]
    
    # Verify the Excel content
    excel_data = io.BytesIO(response.content)
    df = pd.read_excel(excel_data)
    
    # Check that the DataFrame has the expected columns
    expected_columns = ["ID", "Title", "Description", "Reporting Period", "Status", "Organization ID", 
                        "ESRS Compliance", "Materiality Assessment", "Sustainability Targets", "Created At", "Updated At"]
    assert all(col in df.columns for col in expected_columns)

def test_export_comprehensive_excel():
    """Test the comprehensive Excel export endpoint"""
    response = client.get("/api/excel/comprehensive-report")
    
    # Check response status and headers
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    assert "attachment; filename=openfootprint_comprehensive_report.xlsx" in response.headers["Content-Disposition"]
    
    # Verify the Excel content
    excel_data = io.BytesIO(response.content)
    
    # Check that the Excel file has all expected sheets
    excel_file = pd.ExcelFile(excel_data)
    expected_sheets = ["Organizations", "Facilities", "Emission Reports", "CSRD Reports"]
    assert all(sheet in excel_file.sheet_names for sheet in expected_sheets)
    
    # Check content of each sheet
    org_df = pd.read_excel(excel_data, sheet_name="Organizations")
    expected_org_columns = ["ID", "Name", "Description", "Parent Organization", "Created At", "Updated At"]
    assert all(col in org_df.columns for col in expected_org_columns)
    
    facilities_df = pd.read_excel(excel_data, sheet_name="Facilities")
    expected_facilities_columns = ["ID", "Name", "Description", "Address", "City", "Country", "Latitude", "Longitude", "Created At", "Updated At"]
    assert all(col in facilities_df.columns for col in expected_facilities_columns)
    
    emission_df = pd.read_excel(excel_data, sheet_name="Emission Reports")
    expected_emission_columns = ["ID", "Title", "Description", "Reporting Period", "Status", "Organization ID", "Created At", "Updated At"]
    assert all(col in emission_df.columns for col in expected_emission_columns)
    
    csrd_df = pd.read_excel(excel_data, sheet_name="CSRD Reports")
    expected_csrd_columns = ["ID", "Title", "Description", "Reporting Period", "Status", "Organization ID", 
                            "ESRS Compliance", "Materiality Assessment", "Sustainability Targets", "Created At", "Updated At"]
    assert all(col in csrd_df.columns for col in expected_csrd_columns)
