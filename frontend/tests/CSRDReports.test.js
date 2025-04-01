import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import CSRDReports from '../src/pages/CSRDReports';

// Mock the fetch function
global.fetch = jest.fn();

describe('CSRDReports Component', () => {
  beforeEach(() => {
    // Reset the mock before each test
    fetch.mockReset();
    
    // Mock the fetch response for initial data loading
    fetch.mockImplementation(() => 
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve([
          {
            csrd_report_pk: 'namespace:transactional-data--CSRDReport:12345',
            title: 'Annual CSRD Compliance Report 2024',
            description: 'Comprehensive sustainability report following CSRD requirements',
            reporting_period_start: '2024-01-01T00:00:00Z',
            reporting_period_end: '2024-12-31T23:59:59Z',
            organization_id: 'namespace:master-data--Organization:12345',
            report_type: 'Annual',
            status: 'Draft',
            version: '1.0',
            prepared_by: 'Sustainability Department',
            approved_by: null,
            emission_report_ids: [
              'namespace:transactional-data--EmissionReport:12345',
              'namespace:transactional-data--EmissionReport:12346'
            ],
            created_at: '2025-04-01T00:00:00Z',
            updated_at: null
          }
        ])
      })
    );
  });

  test('renders CSRD Reports page title', () => {
    render(
      <BrowserRouter>
        <CSRDReports />
      </BrowserRouter>
    );
    
    // Check if the page title is rendered
    expect(screen.getByText('CSRD Reports')).toBeInTheDocument();
  });

  test('displays loading state initially', () => {
    render(
      <BrowserRouter>
        <CSRDReports />
      </BrowserRouter>
    );
    
    // Check if loading message is displayed
    expect(screen.getByText('Loading CSRD reports...')).toBeInTheDocument();
  });

  test('displays CSRD reports after loading', async () => {
    render(
      <BrowserRouter>
        <CSRDReports />
      </BrowserRouter>
    );
    
    // Wait for the data to load
    await waitFor(() => {
      expect(screen.getByText('Annual CSRD Compliance Report 2024')).toBeInTheDocument();
    });
    
    // Check if report details are displayed
    expect(screen.getByText('Draft')).toBeInTheDocument();
    expect(screen.getByText('Annual')).toBeInTheDocument();
    expect(screen.getByText('1.0')).toBeInTheDocument();
  });

  test('opens form when Create CSRD Report button is clicked', async () => {
    render(
      <BrowserRouter>
        <CSRDReports />
      </BrowserRouter>
    );
    
    // Wait for the data to load
    await waitFor(() => {
      expect(screen.getByText('Annual CSRD Compliance Report 2024')).toBeInTheDocument();
    });
    
    // Click the Create CSRD Report button
    fireEvent.click(screen.getByText('Create CSRD Report'));
    
    // Check if the form is displayed
    expect(screen.getByText('Create New CSRD Report')).toBeInTheDocument();
    expect(screen.getByLabelText('Title')).toBeInTheDocument();
    expect(screen.getByLabelText('Description')).toBeInTheDocument();
    expect(screen.getByLabelText('Reporting Period Start')).toBeInTheDocument();
    expect(screen.getByLabelText('Reporting Period End')).toBeInTheDocument();
    expect(screen.getByLabelText('Organization')).toBeInTheDocument();
    expect(screen.getByLabelText('Report Type')).toBeInTheDocument();
    expect(screen.getByLabelText('Status')).toBeInTheDocument();
    expect(screen.getByLabelText('Version')).toBeInTheDocument();
    expect(screen.getByLabelText('Prepared By')).toBeInTheDocument();
    expect(screen.getByLabelText('Approved By')).toBeInTheDocument();
    expect(screen.getByLabelText('Emission Reports')).toBeInTheDocument();
  });

  test('validates report when Validate button is clicked', async () => {
    render(
      <BrowserRouter>
        <CSRDReports />
      </BrowserRouter>
    );
    
    // Wait for the data to load
    await waitFor(() => {
      expect(screen.getByText('Annual CSRD Compliance Report 2024')).toBeInTheDocument();
    });
    
    // Find and click the Validate button
    const validateButtons = screen.getAllByText('Validate');
    fireEvent.click(validateButtons[0]);
    
    // Check if validation results are displayed
    await waitFor(() => {
      expect(screen.getByText('Validation Results')).toBeInTheDocument();
    });
    
    expect(screen.getByText('PASSED')).toBeInTheDocument();
    expect(screen.getByText('Standards Version:')).toBeInTheDocument();
    expect(screen.getByText('ESRS 2023')).toBeInTheDocument();
    expect(screen.getByText('Compliance Checks')).toBeInTheDocument();
  });

  test('generates report when Generate button is clicked', async () => {
    render(
      <BrowserRouter>
        <CSRDReports />
      </BrowserRouter>
    );
    
    // Wait for the data to load
    await waitFor(() => {
      expect(screen.getByText('Annual CSRD Compliance Report 2024')).toBeInTheDocument();
    });
    
    // Mock window.alert
    const alertMock = jest.spyOn(window, 'alert').mockImplementation(() => {});
    
    // Find and click the Generate button
    const generateButtons = screen.getAllByText('Generate');
    fireEvent.click(generateButtons[0]);
    
    // Check if alert was called with the expected message
    expect(alertMock).toHaveBeenCalledWith(expect.stringContaining('Report generation started for'));
    
    // Restore the original implementation
    alertMock.mockRestore();
  });
});
