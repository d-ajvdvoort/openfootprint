import React, { useState, useEffect } from 'react';
import './EmissionStatements.css';

const EmissionStatements = () => {
  const [emissionStatements, setEmissionStatements] = useState([]);
  const [organizations, setOrganizations] = useState([]);
  const [facilities, setFacilities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({
    emission_statement_pk: '',
    emission_activity_id: '',
    emission_calculation_model_id: '',
    value: '',
    unit: '',
    reporting_period_start: '',
    reporting_period_end: '',
    facility_id: '',
    organization_id: ''
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
      
      // Mock facilities data
      const facs = [
        {
          facility_pk: 'namespace:master-data--Facility:12345',
          name: 'Manufacturing Plant Alpha'
        },
        {
          facility_pk: 'namespace:master-data--Facility:12346',
          name: 'Distribution Center Beta'
        }
      ];
      
      setFacilities(facs);
      
      // Mock emission statements data
      setEmissionStatements([
        {
          emission_statement_pk: 'namespace:transactional-data--EmissionStatement:12345',
          emission_activity_id: 'namespace:master-data--EmissionActivity:67890',
          emission_calculation_model_id: 'namespace:master-data--EmissionCalculationModel:54321',
          value: 1250.5,
          unit: 'kg CO2e',
          reporting_period_start: '2024-01-01T00:00:00Z',
          reporting_period_end: '2024-01-31T23:59:59Z',
          facility_id: 'namespace:master-data--Facility:12345',
          organization_id: 'namespace:master-data--Organization:12345',
          created_at: '2025-04-01T00:00:00Z',
          updated_at: '2025-04-01T01:00:00Z'
        },
        {
          emission_statement_pk: 'namespace:transactional-data--EmissionStatement:12346',
          emission_activity_id: 'namespace:master-data--EmissionActivity:67891',
          emission_calculation_model_id: 'namespace:master-data--EmissionCalculationModel:54322',
          value: 875.2,
          unit: 'kg CO2e',
          reporting_period_start: '2024-02-01T00:00:00Z',
          reporting_period_end: '2024-02-29T23:59:59Z',
          facility_id: 'namespace:master-data--Facility:12345',
          organization_id: 'namespace:master-data--Organization:12345',
          created_at: '2025-04-01T00:00:00Z',
          updated_at: null
        },
        {
          emission_statement_pk: 'namespace:transactional-data--EmissionStatement:12347',
          emission_activity_id: 'namespace:master-data--EmissionActivity:67892',
          emission_calculation_model_id: 'namespace:master-data--EmissionCalculationModel:54323',
          value: 3250.8,
          unit: 'kg CO2e',
          reporting_period_start: '2024-01-01T00:00:00Z',
          reporting_period_end: '2024-01-31T23:59:59Z',
          facility_id: 'namespace:master-data--Facility:12346',
          organization_id: 'namespace:master-data--Organization:12346',
          created_at: '2025-04-01T00:00:00Z',
          updated_at: null
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
    const newStatement = {
      ...formData,
      created_at: new Date().toISOString(),
      updated_at: null
    };
    
    setEmissionStatements([...emissionStatements, newStatement]);
    
    // Reset form
    setFormData({
      emission_statement_pk: '',
      emission_activity_id: '',
      emission_calculation_model_id: '',
      value: '',
      unit: '',
      reporting_period_start: '',
      reporting_period_end: '',
      facility_id: '',
      organization_id: ''
    });
    
    setShowForm(false);
  };

  const getOrganizationName = (orgId) => {
    const org = organizations.find(o => o.organization_pk === orgId);
    return org ? org.name : 'Unknown Organization';
  };

  const getFacilityName = (facId) => {
    const fac = facilities.find(f => f.facility_pk === facId);
    return fac ? fac.name : 'Unknown Facility';
  };

  const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString();
  };

  return (
    <div className="emission-statements-page">
      <div className="page-header">
        <h1>Emission Statements</h1>
        <button 
          className="add-button"
          onClick={() => setShowForm(!showForm)}
        >
          {showForm ? 'Cancel' : 'Add Statement'}
        </button>
      </div>
      
      {showForm && (
        <div className="form-container">
          <h2>Create New Emission Statement</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="emission_statement_pk">Statement ID</label>
              <input
                type="text"
                id="emission_statement_pk"
                name="emission_statement_pk"
                value={formData.emission_statement_pk}
                onChange={handleInputChange}
                required
                placeholder="namespace:transactional-data--EmissionStatement:12348"
              />
            </div>
            
            <div className="form-row">
              <div className="form-group">
                <label htmlFor="emission_activity_id">Emission Activity ID</label>
                <input
                  type="text"
                  id="emission_activity_id"
                  name="emission_activity_id"
                  value={formData.emission_activity_id}
                  onChange={handleInputChange}
                  required
                  placeholder="namespace:master-data--EmissionActivity:67893"
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="emission_calculation_model_id">Calculation Model ID</label>
                <input
                  type="text"
                  id="emission_calculation_model_id"
                  name="emission_calculation_model_id"
                  value={formData.emission_calculation_model_id}
                  onChange={handleInputChange}
                  placeholder="namespace:master-data--EmissionCalculationModel:54324"
                />
              </div>
            </div>
            
            <div className="form-row">
              <div className="form-group">
                <label htmlFor="value">Value</label>
                <input
                  type="number"
                  step="0.01"
                  id="value"
                  name="value"
                  value={formData.value}
                  onChange={handleInputChange}
                  required
                  placeholder="0.00"
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="unit">Unit</label>
                <select
                  id="unit"
                  name="unit"
                  value={formData.unit}
                  onChange={handleInputChange}
                  required
                >
                  <option value="">Select Unit</option>
                  <option value="kg CO2e">kg CO2e</option>
                  <option value="t CO2e">t CO2e</option>
                  <option value="kg CH4">kg CH4</option>
                  <option value="kg N2O">kg N2O</option>
                </select>
              </div>
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
            
            <div className="form-row">
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
              
              <div className="form-group">
                <label htmlFor="facility_id">Facility</label>
                <select
                  id="facility_id"
                  name="facility_id"
                  value={formData.facility_id}
                  onChange={handleInputChange}
                >
                  <option value="">Select Facility (Optional)</option>
                  {facilities.map(fac => (
                    <option key={fac.facility_pk} value={fac.facility_pk}>
                      {fac.name}
                    </option>
                  ))}
                </select>
              </div>
            </div>
            
            <div className="form-actions">
              <button type="submit" className="submit-button">Create Statement</button>
              <button type="button" className="cancel-button" onClick={() => setShowForm(false)}>Cancel</button>
            </div>
          </form>
        </div>
      )}
      
      {loading ? (
        <div className="loading">Loading emission statements...</div>
      ) : (
        <div className="emission-statements-list">
          <table>
            <thead>
              <tr>
                <th>Activity ID</th>
                <th>Value</th>
                <th>Unit</th>
                <th>Reporting Period</th>
                <th>Organization</th>
                <th>Facility</th>
                <th>Created</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {emissionStatements.map(statement => (
                <tr key={statement.emission_statement_pk}>
                  <td>{statement.emission_activity_id.split(':').pop()}</td>
                  <td>{statement.value}</td>
                  <td>{statement.unit}</td>
                  <td>
                    {formatDate(statement.reporting_period_start)} to {formatDate(statement.reporting_period_end)}
                  </td>
                  <td>{getOrganizationName(statement.organization_id)}</td>
                  <td>{statement.facility_id ? getFacilityName(statement.facility_id) : 'N/A'}</td>
                  <td>{formatDate(statement.created_at)}</td>
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

export default EmissionStatements;
