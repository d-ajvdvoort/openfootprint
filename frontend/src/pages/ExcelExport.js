import React from 'react';
import './ExcelExport.css';

const ExcelExport = () => {
  const backendUrl = process.env.REACT_APP_API_URL || 'https://openfootprint-backend.onrender.com/api';
  
  const handleExport = (endpoint) => {
    // Create a temporary link element
    const link = document.createElement('a');
    link.href = `${backendUrl}/excel/${endpoint}`;
    
    // Set the download attribute based on the endpoint
    switch(endpoint) {
      case 'organizations':
        link.download = 'organizations.xlsx';
        break;
      case 'facilities':
        link.download = 'facilities.xlsx';
        break;
      case 'emission-reports':
        link.download = 'emission_reports.xlsx';
        break;
      case 'csrd-reports':
        link.download = 'csrd_reports.xlsx';
        break;
      case 'comprehensive-report':
        link.download = 'openfootprint_comprehensive_report.xlsx';
        break;
      default:
        link.download = 'export.xlsx';
    }
    
    // Append to body, click, and remove
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="excel-export-page">
      <h1>Excel Export</h1>
      <p className="description">
        Export your OpenFootprint data to Excel spreadsheets for further analysis, reporting, and sharing.
      </p>
      
      <div className="export-options">
        <div className="export-card">
          <div className="export-icon">
            <i className="fas fa-building"></i>
          </div>
          <div className="export-content">
            <h3>Organizations</h3>
            <p>Export all organization data including hierarchical structure.</p>
            <button 
              className="export-button"
              onClick={() => handleExport('organizations')}
            >
              Export Organizations
            </button>
          </div>
        </div>
        
        <div className="export-card">
          <div className="export-icon">
            <i className="fas fa-industry"></i>
          </div>
          <div className="export-content">
            <h3>Facilities</h3>
            <p>Export all facility data including locations and details.</p>
            <button 
              className="export-button"
              onClick={() => handleExport('facilities')}
            >
              Export Facilities
            </button>
          </div>
        </div>
        
        <div className="export-card">
          <div className="export-icon">
            <i className="fas fa-file-alt"></i>
          </div>
          <div className="export-content">
            <h3>Emission Reports</h3>
            <p>Export all emission report data and their statuses.</p>
            <button 
              className="export-button"
              onClick={() => handleExport('emission-reports')}
            >
              Export Emission Reports
            </button>
          </div>
        </div>
        
        <div className="export-card">
          <div className="export-icon">
            <i className="fas fa-clipboard-check"></i>
          </div>
          <div className="export-content">
            <h3>CSRD Reports</h3>
            <p>Export all CSRD compliance report data.</p>
            <button 
              className="export-button"
              onClick={() => handleExport('csrd-reports')}
            >
              Export CSRD Reports
            </button>
          </div>
        </div>
        
        <div className="export-card comprehensive">
          <div className="export-icon">
            <i className="fas fa-file-excel"></i>
          </div>
          <div className="export-content">
            <h3>Comprehensive Report</h3>
            <p>Export all data in a single multi-sheet Excel workbook.</p>
            <button 
              className="export-button comprehensive-button"
              onClick={() => handleExport('comprehensive-report')}
            >
              Export Comprehensive Report
            </button>
          </div>
        </div>
      </div>
      
      <div className="export-notes">
        <h3>Notes:</h3>
        <ul>
          <li>Exported files are in Microsoft Excel (.xlsx) format</li>
          <li>All data is current as of the time of export</li>
          <li>Large datasets may take a few moments to generate</li>
          <li>For custom exports or specific data needs, please contact the administrator</li>
        </ul>
      </div>
    </div>
  );
};

export default ExcelExport;
