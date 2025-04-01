import React, { useState, useEffect } from 'react';
import './EmissionReports.css';

const EmissionReports = () => {
  const [emissionReports, setEmissionReports] = useState([]);
  const [organizations, setOrganizations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({
    emission_report_pk: '',
    description: '',
    report_period_start: '',
    report_period_end: '',
    organization_id: '',
    report_type: 'CSRD',
    status: 'Draft'
  });
  const [showForm, setShowForm] = useState(false);

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
      setEmissionReports([
        {
          emission_report_pk: 'namespace:transactional-data--EmissionReport:12345',
          description: 'Annual GHG emissions report for 2024',
          report_period_start: '2024-01-01T00:00:00Z',
          report_period_end: '2024-12-31T23:59:59Z',
          organization_id: 'namespace:master-data--Organization:12345',
          report_type: 'CSRD',
          status: 'Final',
          created_at: '2025-01-15T00:00:00Z',
          updated_at: '2025-02-01T01:00:00Z'
        },
        {
          emission_report_pk: 'namespace:transactional-data--EmissionReport:12346',
          description: 'Q1 2025 emissions report',
          report_period_start: '2025-01-01T00:00:00Z',
          report_period_end: '2025-03-31T23:59:59Z',
          organization_id: 'namespace:master-data--Organization:12345',
          report_type: 'CSRD',
          status: 'Draft',
          created_at: '2025-04-01T00:00:00Z',
          updated_at: null
        },
        {
          emission_report_pk: 'namespace:transactional-data--EmissionReport:12347',
          description: 'Manufacturing Division Annual Report 2024',
          report_period_start: '2024-01-01T00:00:00Z',
          report_period_end: '2024-12-31T23:59:59Z',
          organization_id: 'namespace:master-data--Organization:12346',
          report_type: 'GHG',
          status: 'Submitted',
          created_at: '2025-01-20T00:00:00Z',
          updated_at: '2025-01-25T01:00:00Z'
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
    
    setEmissionReports([...emissionReports, newReport]);
    
    // Reset form
    setFormData({
      emission_report_pk: '',
      description: '',
      report_period_start: '',
      report_period_end: '',
      organization_id: '',
      report_type: 'CSRD',
      status: 'Draft'
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

  return (
    <div className="emission-reports-page">
      <div className="page-header">
        <h1>Emission Reports</h1>
        <button 
          className="add-button"
          onClick={() => setShowForm(!showForm)}
        >
          {showForm ? 'Cancel' : 'Add Report'}
        </button>
      </div>
      
      {showForm && (
        <div className="form-container">
          <h2>Create New Emission Report</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="emission_report_pk">Report ID</label>
              <input
                type="text"
                id="emission_report_pk"
                name="emission_report_pk"
                value={formData.emission_report_pk}
                onChange={handleInputChange}
                required
                placeholder="namespace:transactional-data--EmissionReport:12348"
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
                <label htmlFor="report_period_start">Reporting Period Start</label>
                <input
                  type="date"
                  id="report_period_start"
                  name="report_period_start"
                  value={formData.report_period_start}
                  onChange={handleInputChange}
                  required
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="report_period_end">Reporting Period End</label>
                <input
                  type="date"
                  id="report_period_end"
                  name="report_period_end"
                  value={formData.report_period_end}
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
                  <option value="CSRD">CSRD</option>
                  <option value="GHG">GHG</option>
                  <option value="Annual">Annual</option>
                  <option value="Quarterly">Quarterly</option>
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
                  <option value="Final">Final</option>
                  <option value="Submitted">Submitted</option>
                  <option value="Verified">Verified</option>
                </select>
              </div>
            </div>
            
            <div className="form-actions">
              <button type="submit" className="submit-button">Create Report</button>
              <button type="button" className="cancel-button" onClick={() => setShowForm(false)}>Cancel</button>
            </div>
          </form>
        </div>
      )}
      
      {loading ? (
        <div className="loading">Loading emission reports...</div>
      ) : (
        <div className="emission-reports-list">
          <table>
            <thead>
              <tr>
                <th>Description</th>
                <th>Organization</th>
                <th>Reporting Period</th>
                <th>Type</th>
                <th>Status</th>
                <th>Created</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {emissionReports.map(report => (
                <tr key={report.emission_report_pk}>
                  <td>{report.description}</td>
                  <td>{getOrganizationName(report.organization_id)}</td>
                  <td>
                    {formatDate(report.report_period_start)} to {formatDate(report.report_period_end)}
                  </td>
                  <td>{report.report_type}</td>
                  <td>
                    <span className={`status-badge ${report.status.toLowerCase()}`}>
                      {report.status}
                    </span>
                  </td>
                  <td>{formatDate(report.created_at)}</td>
                  <td>
                    <button className="action-button">Edit</button>
                    <button className="action-button view">View</button>
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

export default EmissionReports;
