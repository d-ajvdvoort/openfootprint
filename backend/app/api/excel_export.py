import pandas as pd
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.database import get_db
from app.models.organization import Organization
from app.models.facility import Facility
from app.models.emission_report import EmissionReport
from app.models.emission_statement import EmissionStatement
from app.models.csrd_report import CSRDReport
from app.services.organization_service import OrganizationService
from app.services.facility_service import FacilityService
from app.services.emission_report_service import EmissionReportService
from app.services.csrd_report_service import CSRDReportService

router = APIRouter(
    prefix="/api/excel",
    tags=["excel"],
    responses={404: {"description": "Not found"}},
)

@router.get("/organizations")
def export_organizations_excel(
    db: Session = Depends(get_db),
    organization_service: OrganizationService = Depends()
):
    """Export organizations data as Excel spreadsheet"""
    organizations = organization_service.get_organizations(db)
    
    # Convert to DataFrame
    data = []
    for org in organizations:
        data.append({
            "ID": org.organization_pk,
            "Name": org.name,
            "Description": org.description,
            "Parent Organization": org.parent_organization_id,
            "Created At": org.created_at,
            "Updated At": org.updated_at
        })
    
    df = pd.DataFrame(data)
    
    # Create Excel file in memory
    output = pd.ExcelWriter('organizations.xlsx', engine='xlsxwriter')
    df.to_excel(output, sheet_name='Organizations', index=False)
    
    # Configure the sheet
    workbook = output.book
    worksheet = output.sheets['Organizations']
    
    # Add formatting
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1
    })
    
    # Write the column headers with the defined format
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
        worksheet.set_column(col_num, col_num, 20)
    
    # Close the Pandas Excel writer and output the Excel file
    output.close()
    
    # Return the Excel file as a downloadable attachment
    with open('organizations.xlsx', 'rb') as f:
        excel_data = f.read()
    
    return Response(
        content=excel_data,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=organizations.xlsx"}
    )

@router.get("/facilities")
def export_facilities_excel(
    db: Session = Depends(get_db),
    facility_service: FacilityService = Depends()
):
    """Export facilities data as Excel spreadsheet"""
    facilities = facility_service.get_facilities(db)
    
    # Convert to DataFrame
    data = []
    for facility in facilities:
        data.append({
            "ID": facility.facility_pk,
            "Name": facility.name,
            "Description": facility.description,
            "Address": facility.address,
            "City": facility.city,
            "Country": facility.country,
            "Latitude": facility.latitude,
            "Longitude": facility.longitude,
            "Created At": facility.created_at,
            "Updated At": facility.updated_at
        })
    
    df = pd.DataFrame(data)
    
    # Create Excel file in memory
    output = pd.ExcelWriter('facilities.xlsx', engine='xlsxwriter')
    df.to_excel(output, sheet_name='Facilities', index=False)
    
    # Configure the sheet
    workbook = output.book
    worksheet = output.sheets['Facilities']
    
    # Add formatting
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1
    })
    
    # Write the column headers with the defined format
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
        worksheet.set_column(col_num, col_num, 20)
    
    # Close the Pandas Excel writer and output the Excel file
    output.close()
    
    # Return the Excel file as a downloadable attachment
    with open('facilities.xlsx', 'rb') as f:
        excel_data = f.read()
    
    return Response(
        content=excel_data,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=facilities.xlsx"}
    )

@router.get("/emission-reports")
def export_emission_reports_excel(
    db: Session = Depends(get_db),
    emission_report_service: EmissionReportService = Depends()
):
    """Export emission reports data as Excel spreadsheet"""
    reports = emission_report_service.get_emission_reports(db)
    
    # Convert to DataFrame
    data = []
    for report in reports:
        data.append({
            "ID": report.emission_report_pk,
            "Title": report.title,
            "Description": report.description,
            "Reporting Period": report.reporting_period,
            "Status": report.status,
            "Organization ID": report.organization_id,
            "Created At": report.created_at,
            "Updated At": report.updated_at
        })
    
    df = pd.DataFrame(data)
    
    # Create Excel file in memory
    output = pd.ExcelWriter('emission_reports.xlsx', engine='xlsxwriter')
    df.to_excel(output, sheet_name='Emission Reports', index=False)
    
    # Configure the sheet
    workbook = output.book
    worksheet = output.sheets['Emission Reports']
    
    # Add formatting
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1
    })
    
    # Write the column headers with the defined format
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
        worksheet.set_column(col_num, col_num, 20)
    
    # Close the Pandas Excel writer and output the Excel file
    output.close()
    
    # Return the Excel file as a downloadable attachment
    with open('emission_reports.xlsx', 'rb') as f:
        excel_data = f.read()
    
    return Response(
        content=excel_data,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=emission_reports.xlsx"}
    )

@router.get("/csrd-reports")
def export_csrd_reports_excel(
    db: Session = Depends(get_db),
    csrd_report_service: CSRDReportService = Depends()
):
    """Export CSRD reports data as Excel spreadsheet"""
    reports = csrd_report_service.get_csrd_reports(db)
    
    # Convert to DataFrame
    data = []
    for report in reports:
        data.append({
            "ID": report.csrd_report_pk,
            "Title": report.title,
            "Description": report.description,
            "Reporting Period": report.reporting_period,
            "Status": report.status,
            "Organization ID": report.organization_id,
            "ESRS Compliance": report.esrs_compliance,
            "Materiality Assessment": report.materiality_assessment,
            "Sustainability Targets": report.sustainability_targets,
            "Created At": report.created_at,
            "Updated At": report.updated_at
        })
    
    df = pd.DataFrame(data)
    
    # Create Excel file in memory
    output = pd.ExcelWriter('csrd_reports.xlsx', engine='xlsxwriter')
    df.to_excel(output, sheet_name='CSRD Reports', index=False)
    
    # Configure the sheet
    workbook = output.book
    worksheet = output.sheets['CSRD Reports']
    
    # Add formatting
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1
    })
    
    # Write the column headers with the defined format
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
        worksheet.set_column(col_num, col_num, 20)
    
    # Close the Pandas Excel writer and output the Excel file
    output.close()
    
    # Return the Excel file as a downloadable attachment
    with open('csrd_reports.xlsx', 'rb') as f:
        excel_data = f.read()
    
    return Response(
        content=excel_data,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=csrd_reports.xlsx"}
    )

@router.get("/comprehensive-report")
def export_comprehensive_excel(
    db: Session = Depends(get_db),
    organization_service: OrganizationService = Depends(),
    facility_service: FacilityService = Depends(),
    emission_report_service: EmissionReportService = Depends(),
    csrd_report_service: CSRDReportService = Depends()
):
    """Export comprehensive data as multi-sheet Excel spreadsheet"""
    # Get all data
    organizations = organization_service.get_organizations(db)
    facilities = facility_service.get_facilities(db)
    emission_reports = emission_report_service.get_emission_reports(db)
    csrd_reports = csrd_report_service.get_csrd_reports(db)
    
    # Create Excel file with multiple sheets
    output = pd.ExcelWriter('openfootprint_comprehensive_report.xlsx', engine='xlsxwriter')
    
    # Organizations sheet
    org_data = []
    for org in organizations:
        org_data.append({
            "ID": org.organization_pk,
            "Name": org.name,
            "Description": org.description,
            "Parent Organization": org.parent_organization_id,
            "Created At": org.created_at,
            "Updated At": org.updated_at
        })
    
    org_df = pd.DataFrame(org_data)
    org_df.to_excel(output, sheet_name='Organizations', index=False)
    
    # Facilities sheet
    facility_data = []
    for facility in facilities:
        facility_data.append({
            "ID": facility.facility_pk,
            "Name": facility.name,
            "Description": facility.description,
            "Address": facility.address,
            "City": facility.city,
            "Country": facility.country,
            "Latitude": facility.latitude,
            "Longitude": facility.longitude,
            "Created At": facility.created_at,
            "Updated At": facility.updated_at
        })
    
    facility_df = pd.DataFrame(facility_data)
    facility_df.to_excel(output, sheet_name='Facilities', index=False)
    
    # Emission Reports sheet
    emission_data = []
    for report in emission_reports:
        emission_data.append({
            "ID": report.emission_report_pk,
            "Title": report.title,
            "Description": report.description,
            "Reporting Period": report.reporting_period,
            "Status": report.status,
            "Organization ID": report.organization_id,
            "Created At": report.created_at,
            "Updated At": report.updated_at
        })
    
    emission_df = pd.DataFrame(emission_data)
    emission_df.to_excel(output, sheet_name='Emission Reports', index=False)
    
    # CSRD Reports sheet
    csrd_data = []
    for report in csrd_reports:
        csrd_data.append({
            "ID": report.csrd_report_pk,
            "Title": report.title,
            "Description": report.description,
            "Reporting Period": report.reporting_period,
            "Status": report.status,
            "Organization ID": report.organization_id,
            "ESRS Compliance": report.esrs_compliance,
            "Materiality Assessment": report.materiality_assessment,
            "Sustainability Targets": report.sustainability_targets,
            "Created At": report.created_at,
            "Updated At": report.updated_at
        })
    
    csrd_df = pd.DataFrame(csrd_data)
    csrd_df.to_excel(output, sheet_name='CSRD Reports', index=False)
    
    # Format all sheets
    workbook = output.book
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1
    })
    
    # Apply formatting to each sheet
    for sheet_name in ['Organizations', 'Facilities', 'Emission Reports', 'CSRD Reports']:
        worksheet = output.sheets[sheet_name]
        df = None
        
        if sheet_name == 'Organizations':
            df = org_df
        elif sheet_name == 'Facilities':
            df = facility_df
        elif sheet_name == 'Emission Reports':
            df = emission_df
        elif sheet_name == 'CSRD Reports':
            df = csrd_df
            
        # Write headers with formatting
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)
            worksheet.set_column(col_num, col_num, 20)
    
    # Close the Pandas Excel writer and output the Excel file
    output.close()
    
    # Return the Excel file as a downloadable attachment
    with open('openfootprint_comprehensive_report.xlsx', 'rb') as f:
        excel_data = f.read()
    
    return Response(
        content=excel_data,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=openfootprint_comprehensive_report.xlsx"}
    )
