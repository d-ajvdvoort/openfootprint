import React, { useState, useEffect } from 'react';
import './CSRDReports.css';

const CSRDReports = () => {
  const [csrdReports, setCSRDReports] = useState([]);
  const [organizations, setOrganizations] = useState([]);
  const [emissionReports, setEmissionReports] = useState([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({
    csrd_report_pk: '',
    title: '',
    description: '',
    reporting_period_start: '',
    reporting_period_end: '',
    organization_id: '',
    report_type: 'Annual',
    status: 'Draft',
    version: '1.0',
    prepared_by: '',
    approved_by: '',
    emission_report_ids: []
  });
  const [showForm, setShowForm] = useState(false);
  const [validationResults, setValidationResults] = useState(null);
  const [showValidation, setShowValidation] = useState(false);

  useEffect(() => {
    // In a real implementation, this would fetch data from the API
    // Simulating API call with setTimeout
    setTimeout(() => {
      // Mock organizations data
      const orgs = [
        {
          organization_pk: 'namespace:master-data--Organization:12345',
          name: 'Example Corporation'
        },
        {
          organization_pk: 'namespace:master-data--Organization:12346',
          name: 'Manufacturing Division'
        }
      ];
      
      setOrganizations(orgs);
      
      // Mock emission reports data
      const emissionReps = [
        {
          emission_report_pk: 'namespace:transactional-data--EmissionReport:12345',
          description: 'Annual GHG emissions report for 2024',
          organization_id: 'namespace:master-data--Organization:12345'
        },
        {
          emission_report_pk: 'namespace:transactional-data--EmissionReport:12346',
          description: 'Q1 2025 emissions report',
          organization_id: 'namespace:master-data--Organization:12345'
        },
        {
          emission_report_pk: 'namespace:transactional-data--EmissionReport:12347',
          description: 'Manufacturing Division Annual Report 2024',
          organization_id: 'namespace:master-data--Organization:12346'
        }
      ];
      
      setEmissionReports(emissionReps);
      
      // Mock CSRD reports data
      setCSRDReports([
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
        },
        {
          csrd_report_pk: 'namespace:transactional-data--CSRDReport:12346',
          title: 'Manufacturing Division CSRD Report 2024',
          description: 'CSRD report for manufacturing operations',
          reporting_period_start: '2024-01-01T00:00:00Z',
          reporting_period_end: '2024-12-31T23:59:59Z',
          organization_id: 'namespace:master-data--Organization:12346',
          report_type: 'Annual',
          status: 'In Review',
          version: '1.2',
          prepared_by: 'Manufacturing Sustainability Team',
          approved_by: 'Sustainability Director',
          emission_report_ids: [
            'namespace:transactional-data--EmissionReport:12347'
          ],
          created_at: '2025-03-15T00:00:00Z',
          updated_at: '2025-03-20T00:00:00Z'
        }
      ]);
      
      setLoading(false);
    }, 1000);
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleEmissionReportSelection = (e) => {
    const options = e.target.options;
    const selectedValues = [];
    for (let i = 0; i < options.length; i++) {
      if (options[i].selected) {
        selectedValues.push(options[i].value);
      }
    }
    setFormData({
      ...formData,
      emission_report_ids: selectedValues
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // In a real implementation, this would send data to the API
    console.log('Form submitted:', formData);
    
    // Simulate adding to the list
    const newReport = {
      ...formData,
      created_at: new Date().toISOString(),
      updated_at: null
    };
    
    setCSRDReports([...csrdReports, newReport]);
    
    // Reset form
    setFormData({
      csrd_report_pk: '',
      title: '',
      description: '',
      reporting_period_start: '',
      reporting_period_end: '',
      organization_id: '',
      report_type: 'Annual',
      status: 'Draft',
      version: '1.0',
      prepared_by: '',
      approved_by: '',
      emission_report_ids: []
    });
    
    setShowForm(false);
  };

  const getOrganizationName = (orgId) => {
    const org = organizations.find(o => o.organization_pk === orgId);
    return org ? org.name : 'Unknown Organization';
  };

  const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString();
  };

  const handleGenerateReport = (reportId) => {
    // In a real implementation, this would call the API to generate a report
    console.log('Generating report for:', reportId);
    alert(`Report generation started for ${reportId}. The document will be available for download shortly.`);
  };

  const handleValidateReport = (reportId) => {
    // In a real implementation, this would call the API to validate a report
    console.log('Validating report:', reportId);
    
    // Mock validation results
    const mockValidationResults = {
      overall_status: "passed",
      validation_date: new Date().toISOString(),
      standards_version: "ESRS 2023",
      checks: [
        {
          standard: "ESRS E1",
          description: "Climate change",
          status: "passed",
          details: "All required climate change disclosures are present"
        },
        {
          standard: "ESRS E2",
          description: "Pollution",
          status: "warning",
          details: "Some pollution metrics may need additional context"
        },
        {
          standard: "ESRS S1",
          description: "Own workforce",
          status: "passed",
          details: "Workforce disclosures are complete"
        }
      ]
    };
    
    setValidationResults(mockValidationResults);
    setShowValidation(true);
  };

  return (
    <div className="csrd-reports-page">
      <div className="page-header">
        <h1>CSRD Reports</h1>
        <button 
          className="add-button"
          onClick={() => setShowForm(!showForm)}
        >
          {showForm ? 'Cancel' : 'Create CSRD Report'}
        </button>
      </div>
      
      {showForm && (
        <div className="form-container">
          <h2>Create New CSRD Report</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="csrd_report_pk">Report ID</label>
              <input
                type="text"
                id="csrd_report_pk"
                name="csrd_report_pk"
                value={formData.csrd_report_pk}
                onChange={handleInputChange}
                required
                placeholder="namespace:transactional-data--CSRDReport:12347"
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="title">Title</label>
              <input
                type="text"
                id="title"
                name="title"
                value={formData.title}
                onChange={handleInputChange}
                required
                placeholder="CSRD Report Title"
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="description">Description</label>
              <textarea
                id="description"
                name="description"
                value={formData.description}
                onChange={handleInputChange}
                placeholder="Report Description"
              />
            </div>
            
            <div className="form-row">
              <div className="form-group">
                <label htmlFor="reporting_period_start">Reporting Period Start</label>
                <input
                  type="date"
                  id="reporting_period_start"
                  name="reporting_period_start"
                  value={formData.reporting_period_start}
                  onChange={handleInputChange}
                  required
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="reporting_period_end">Reporting Period End</label>
                <input
                  type="date"
                  id="reporting_period_end"
                  name="reporting_period_end"
                  value={formData.reporting_period_end}
                  onChange={handleInputChange}
                  required
                />
              </div>
            </div>
            
            <div className="form-group">
              <label htmlFor="organization_id">Organization</label>
              <select
                id="organization_id"
                name="organization_id"
                value={formData.organization_id}
                onChange={handleInputChange}
                required
              >
                <option value="">Select Organization</option>
                {organizations.map(org => (
                  <option key={org.organization_pk} value={org.organization_pk}>
                    {org.name}
                  </option>
                ))}
              </select>
            </div>
            
            <div className="form-row">
              <div className="form-group">
                <label htmlFor="report_type">Report Type</label>
                <select
                  id="report_type"
                  name="report_type"
                  value={formData.report_type}
                  onChange={handleInputChange}
                  required
                >
                  <option value="Annual">Annual</option>
                  <option value="Interim">Interim</option>
                  <option value="Supplementary">Supplementary</option>
                </select>
              </div>
              
              <div className="form-group">
                <label htmlFor="status">Status</label>
                <select
                  id="status"
                  name="status"
                  value={formData.status}
                  onChange={handleInputChange}
                  required
                >
                  <option value="Draft">Draft</option>
                  <option value="In Review">In Review</option>
                  <option value="Approved">Approved</option>
                  <option value="Published">Published</option>
                  <option value="Submitted">Submitted</option>
                </select>
              </div>
            </div>
            
            <div className="form-row">
              <div className="form-group">
                <label htmlFor="version">Version</label>
                <input
                  type="text"
                  id="version"
                  name="version"
                  value={formData.version}
                  onChange={handleInputChange}
                  required
                  placeholder="1.0"
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="prepared_by">Prepared By</label>
                <input
                  type="text"
                  id="prepared_by"
                  name="prepared_by"
                  value={formData.prepared_by}
                  onChange={handleInputChange}
                  required
                  placeholder="Sustainability Department"
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="approved_by">Approved By</label>
                <input
                  type="text"
                  id="approved_by"
                  name="approved_by"
                  value={formData.approved_by}
                  onChange={handleInputChange}
                  placeholder="Sustainability Director"
                />
              </div>
            </div>
            
            <div className="form-group">
              <label htmlFor="emission_report_ids">Emission Reports</label>
              <select
                id="emission_report_ids"
                name="emission_report_ids"
                multiple
                value={formData.emission_report_ids}
                onChange={handleEmissionReportSelection}
                required
                className="multi-select"
              >
                {emissionReports.map(report => (
                  <option key={report.emission_report_pk} value={report.emission_report_pk}>
                    {report.description}
                  </option>
                ))}
              </select>
              <small className="form-help">Hold Ctrl (or Cmd on Mac) to select multiple reports</small>
            </div>
            
            <div className="form-actions">
              <button type="submit" className="submit-button">Create CSRD Report</button>
              <button type="button" className="cancel-button" onClick={() => setShowForm(false)}>Cancel</button>
            </div>
          </form>
        </div>
      )}
      
      {showValidation && validationResults && (
        <div className="validation-results">
          <div className="validation-header">
            <h2>Validation Results</h2>
            <button className="close-button" onClick={() => setShowValidation(false)}>×</button>
          </div>
          
          <div className="validation-summary">
            <div className={`validation-status ${validationResults.overall_status}`}>
              {validationResults.overall_status.toUpperCase()}
            </div>
            <div className="validation-info">
              <p><strong>Standards Version:</strong> {validationResults.standards_version}</p>
              <p><strong>Validation Date:</strong> {formatDate(validationResults.validation_date)}</p>
            </div>
          </div>
          
          <div className="validation-checks">
            <h3>Compliance Checks</h3>
            <table>
              <thead>
                <tr>
                  <th>Standard</th>
                  <th>Description</th>
                  <th>Status</th>
                  <th>Details</th>
                </tr>
              </thead>
              <tbody>
                {validationResults.checks.map((check, index) => (
                  <tr key={index}>
                    <td>{check.standard}</td>
                    <td>{check.description}</td>
                    <td>
                      <span className={`check-status ${check.status}`}>
                        {check.status}
                      </span>
                    </td>
                    <td>{check.details}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          
          <div className="validation-actions">
            <button className="action-button">Download Validation Report</button>
            <button className="cancel-button" onClick={() => setShowValidation(false)}>Close</button>
          </div>
        </div>
      )}
      
      {loading ? (
        <div className="loading">Loading CSRD reports...</div>
      ) : (
        <div className="csrd-reports-list">
          <table>
            <thead>
              <tr>
                <th>Title</th>
                <th>Organization</th>
                <th>Reporting Period</th>
                <th>Type</th>
                <th>Status</th>
                <th>Version</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {csrdReports.map(report => (
                <tr key={report.csrd_report_pk}>
                  <td>{report.title}</td>
                  <td>{getOrganizationName(report.organization_id)}</td>
                  <td>
                    {formatDate(report.reporting_period_start)} to {formatDate(report.reporting_period_end)}
                  </td>
                  <td>{report.report_type}</td>
                  <td>
                    <span className={`status-badge ${report.status.toLowerCase().replace(' ', '-')}`}>
                      {report.status}
                    </span>
                  </td>
                  <td>{report.version}</td>
                  <td>
                    <button className="action-button">Edit</button>
                    <button 
                      className="action-button generate"
                      onClick={() => handleGenerateReport(report.csrd_report_pk)}
                    >
                      Generate
                    </button>
                    <button 
                      className="action-button validate"
                      onClick={() => handleValidateReport(report.csrd_report_pk)}
                    >
                      Validate
                    </button>
                    <button className="action-button delete">Delete</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default CSRDReports;
