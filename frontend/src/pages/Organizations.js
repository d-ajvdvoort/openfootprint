import React, { useState, useEffect } from 'react';
import './Organizations.css';

const Organizations = () => {
  const [organizations, setOrganizations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({
    organization_pk: '',
    name: '',
    description: '',
    parent_organization_id: ''
  });
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    // In a real implementation, this would fetch data from the API
    // Simulating API call with setTimeout
    setTimeout(() => {
      setOrganizations([
        {
          organization_pk: 'namespace:master-data--Organization:12345',
          name: 'Example Corporation',
          description: 'A global company focused on sustainability',
          parent_organization_id: null,
          created_at: '2025-04-01T00:00:00Z',
          updated_at: '2025-04-01T01:00:00Z'
        },
        {
          organization_pk: 'namespace:master-data--Organization:12346',
          name: 'Manufacturing Division',
          description: 'Manufacturing operations across Europe',
          parent_organization_id: 'namespace:master-data--Organization:12345',
          created_at: '2025-04-01T00:00:00Z',
          updated_at: '2025-04-01T01:00:00Z'
        },
        {
          organization_pk: 'namespace:master-data--Organization:12347',
          name: 'Distribution Division',
          description: 'Global distribution network',
          parent_organization_id: 'namespace:master-data--Organization:12345',
          created_at: '2025-04-01T00:00:00Z',
          updated_at: '2025-04-01T01:00:00Z'
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
    const newOrg = {
      ...formData,
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString()
    };
    
    setOrganizations([...organizations, newOrg]);
    
    // Reset form
    setFormData({
      organization_pk: '',
      name: '',
      description: '',
      parent_organization_id: ''
    });
    
    setShowForm(false);
  };

  return (
    <div className="organizations-page">
      <div className="page-header">
        <h1>Organizations</h1>
        <button 
          className="add-button"
          onClick={() => setShowForm(!showForm)}
        >
          {showForm ? 'Cancel' : 'Add Organization'}
        </button>
      </div>
      
      {showForm && (
        <div className="form-container">
          <h2>Add New Organization</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="organization_pk">Organization ID</label>
              <input
                type="text"
                id="organization_pk"
                name="organization_pk"
                value={formData.organization_pk}
                onChange={handleInputChange}
                required
                placeholder="namespace:master-data--Organization:12348"
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="name">Name</label>
              <input
                type="text"
                id="name"
                name="name"
                value={formData.name}
                onChange={handleInputChange}
                required
                placeholder="Organization Name"
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="description">Description</label>
              <textarea
                id="description"
                name="description"
                value={formData.description}
                onChange={handleInputChange}
                placeholder="Organization Description"
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="parent_organization_id">Parent Organization ID</label>
              <select
                id="parent_organization_id"
                name="parent_organization_id"
                value={formData.parent_organization_id || ''}
                onChange={handleInputChange}
              >
                <option value="">None (Top-level Organization)</option>
                {organizations.map(org => (
                  <option key={org.organization_pk} value={org.organization_pk}>
                    {org.name}
                  </option>
                ))}
              </select>
            </div>
            
            <div className="form-actions">
              <button type="submit" className="submit-button">Add Organization</button>
              <button type="button" className="cancel-button" onClick={() => setShowForm(false)}>Cancel</button>
            </div>
          </form>
        </div>
      )}
      
      {loading ? (
        <div className="loading">Loading organizations...</div>
      ) : (
        <div className="organizations-list">
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Parent Organization</th>
                <th>Created</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {organizations.map(org => (
                <tr key={org.organization_pk}>
                  <td>{org.name}</td>
                  <td>{org.description}</td>
                  <td>
                    {org.parent_organization_id ? 
                      organizations.find(o => o.organization_pk === org.parent_organization_id)?.name || 'Unknown' 
                      : 'None'}
                  </td>
                  <td>{new Date(org.created_at).toLocaleDateString()}</td>
                  <td>
                    <button className="action-button">Edit</button>
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

export default Organizations;
