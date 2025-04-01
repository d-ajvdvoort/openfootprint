import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import ExcelExport from '../src/pages/ExcelExport';

// Mock the environment variable
jest.mock('process.env', () => ({
  REACT_APP_API_URL: 'https://openfootprint-backend.onrender.com/api'
}));

// Mock document.createElement and other DOM methods
document.createElement = jest.fn().mockImplementation((tag) => {
  if (tag === 'a') {
    return {
      href: '',
      download: '',
      click: jest.fn(),
      appendChild: jest.fn(),
      removeChild: jest.fn()
    };
  }
  return document.createElement(tag);
});

document.body.appendChild = jest.fn();
document.body.removeChild = jest.fn();

describe('ExcelExport Component', () => {
  beforeEach(() => {
    // Reset mocks before each test
    jest.clearAllMocks();
    
    // Render the component within a Router
    render(
      <BrowserRouter>
        <ExcelExport />
      </BrowserRouter>
    );
  });

  test('renders the Excel Export page title', () => {
    const titleElement = screen.getByText(/Excel Export/i);
    expect(titleElement).toBeInTheDocument();
  });

  test('renders all export option cards', () => {
    expect(screen.getByText(/Organizations/i)).toBeInTheDocument();
    expect(screen.getByText(/Facilities/i)).toBeInTheDocument();
    expect(screen.getByText(/Emission Reports/i)).toBeInTheDocument();
    expect(screen.getByText(/CSRD Reports/i)).toBeInTheDocument();
    expect(screen.getByText(/Comprehensive Report/i)).toBeInTheDocument();
  });

  test('clicking Organizations export button triggers download', () => {
    const exportButton = screen.getByText(/Export Organizations/i);
    fireEvent.click(exportButton);
    
    // Check if link was created and clicked
    expect(document.createElement).toHaveBeenCalledWith('a');
    const mockAnchor = document.createElement('a');
    expect(mockAnchor.href).toBe('https://openfootprint-backend.onrender.com/api/excel/organizations');
    expect(mockAnchor.download).toBe('organizations.xlsx');
    expect(document.body.appendChild).toHaveBeenCalled();
    expect(mockAnchor.click).toHaveBeenCalled();
    expect(document.body.removeChild).toHaveBeenCalled();
  });

  test('clicking Facilities export button triggers download', () => {
    const exportButton = screen.getByText(/Export Facilities/i);
    fireEvent.click(exportButton);
    
    // Check if link was created and clicked
    expect(document.createElement).toHaveBeenCalledWith('a');
    const mockAnchor = document.createElement('a');
    expect(mockAnchor.href).toBe('https://openfootprint-backend.onrender.com/api/excel/facilities');
    expect(mockAnchor.download).toBe('facilities.xlsx');
    expect(document.body.appendChild).toHaveBeenCalled();
    expect(mockAnchor.click).toHaveBeenCalled();
    expect(document.body.removeChild).toHaveBeenCalled();
  });

  test('clicking Emission Reports export button triggers download', () => {
    const exportButton = screen.getByText(/Export Emission Reports/i);
    fireEvent.click(exportButton);
    
    // Check if link was created and clicked
    expect(document.createElement).toHaveBeenCalledWith('a');
    const mockAnchor = document.createElement('a');
    expect(mockAnchor.href).toBe('https://openfootprint-backend.onrender.com/api/excel/emission-reports');
    expect(mockAnchor.download).toBe('emission_reports.xlsx');
    expect(document.body.appendChild).toHaveBeenCalled();
    expect(mockAnchor.click).toHaveBeenCalled();
    expect(document.body.removeChild).toHaveBeenCalled();
  });

  test('clicking CSRD Reports export button triggers download', () => {
    const exportButton = screen.getByText(/Export CSRD Reports/i);
    fireEvent.click(exportButton);
    
    // Check if link was created and clicked
    expect(document.createElement).toHaveBeenCalledWith('a');
    const mockAnchor = document.createElement('a');
    expect(mockAnchor.href).toBe('https://openfootprint-backend.onrender.com/api/excel/csrd-reports');
    expect(mockAnchor.download).toBe('csrd_reports.xlsx');
    expect(document.body.appendChild).toHaveBeenCalled();
    expect(mockAnchor.click).toHaveBeenCalled();
    expect(document.body.removeChild).toHaveBeenCalled();
  });

  test('clicking Comprehensive Report export button triggers download', () => {
    const exportButton = screen.getByText(/Export Comprehensive Report/i);
    fireEvent.click(exportButton);
    
    // Check if link was created and clicked
    expect(document.createElement).toHaveBeenCalledWith('a');
    const mockAnchor = document.createElement('a');
    expect(mockAnchor.href).toBe('https://openfootprint-backend.onrender.com/api/excel/comprehensive-report');
    expect(mockAnchor.download).toBe('openfootprint_comprehensive_report.xlsx');
    expect(document.body.appendChild).toHaveBeenCalled();
    expect(mockAnchor.click).toHaveBeenCalled();
    expect(document.body.removeChild).toHaveBeenCalled();
  });
});
