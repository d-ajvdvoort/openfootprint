import React, { useState, useEffect } from 'react';
import './Facilities.css';

const Facilities = () => {
  const [facilities, setFacilities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [formData, setFormData] = useState({
    facility_pk: '',
    name: '',
    description: '',
    address: '',
    city: '',
    country: '',
    latitude: '',
    longitude: ''
  });
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    // In a real implementation, this would fetch data from the API
    // Simulating API call with setTimeout
    setTimeout(() => {
      setFacilities([
        {
          facility_pk: 'namespace:master-data--Facility:12345',
          name: 'Manufacturing Plant Alpha',
          description: 'Main manufacturing facility for consumer products',
          address: '123 Industrial Way',
          city: 'Springfield',
          country: 'United States',
          latitude: 37.7749,
          longitude: -122.4194,
          created_at: '2025-04-01T00:00:00Z',
          updated_at: '2025-04-01T01:00:00Z'
        },
        {
          facility_pk: 'namespace:master-data--Facility:12346',
          name: 'Distribution Center Beta',
          description: 'Regional distribution center for North America',
          address: '456 Logistics Blvd',
          city: 'Chicago',
          country: 'United States',
          latitude: 41.8781,
          longitude: -87.6298,
          created_at: '2025-04-01T00:00:00Z',
          updated_at: '2025-04-01T01:00:00Z'
        },
        {
          facility_pk: 'namespace:master-data--Facility:12347',
          name: 'European Operations HQ',
          description: 'European headquarters and manufacturing',
          address: '78 Industrial Park',
          city: 'Munich',
          country: 'Germany',
          latitude: 48.1351,
          longitude: 11.5820,
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
    const newFacility = {
      ...formData,
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString()
    };
    
    setFacilities([...facilities, newFacility]);
    
    // Reset form
    setFormData({
      facility_pk: '',
      name: '',
      description: '',
      address: '',
      city: '',
      country: '',
      latitude: '',
      longitude: ''
    });
    
    setShowForm(false);
  };

  return (
    <div className="facilities-page">
      <div className="page-header">
        <h1>Facilities</h1>
        <button 
          className="add-button"
          onClick={() => setShowForm(!showForm)}
        >
          {showForm ? 'Cancel' : 'Add Facility'}
        </button>
      </div>
      
      {showForm && (
        <div className="form-container">
          <h2>Add New Facility</h2>
          <form onSubmit={handleSubmit}>
            <div className="form-group">
              <label htmlFor="facility_pk">Facility ID</label>
              <input
                type="text"
                id="facility_pk"
                name="facility_pk"
                value={formData.facility_pk}
                onChange={handleInputChange}
                required
                placeholder="namespace:master-data--Facility:12348"
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
                placeholder="Facility Name"
              />
            </div>
            
            <div className="form-group">
              <label htmlFor="description">Description</label>
              <textarea
                id="description"
                name="description"
                value={formData.description}
                onChange={handleInputChange}
                placeholder="Facility Description"
              />
            </div>
            
            <div className="form-row">
              <div className="form-group">
                <label htmlFor="address">Address</label>
                <input
                  type="text"
                  id="address"
                  name="address"
                  value={formData.address}
                  onChange={handleInputChange}
                  placeholder="Street Address"
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="city">City</label>
                <input
                  type="text"
                  id="city"
                  name="city"
                  value={formData.city}
                  onChange={handleInputChange}
                  placeholder="City"
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="country">Country</label>
                <input
                  type="text"
                  id="country"
                  name="country"
                  value={formData.country}
                  onChange={handleInputChange}
                  placeholder="Country"
                />
              </div>
            </div>
            
            <div className="form-row">
              <div className="form-group">
                <label htmlFor="latitude">Latitude</label>
                <input
                  type="number"
                  step="0.0001"
                  id="latitude"
                  name="latitude"
                  value={formData.latitude}
                  onChange={handleInputChange}
                  placeholder="Latitude"
                />
              </div>
              
              <div className="form-group">
                <label htmlFor="longitude">Longitude</label>
                <input
                  type="number"
                  step="0.0001"
                  id="longitude"
                  name="longitude"
                  value={formData.longitude}
                  onChange={handleInputChange}
                  placeholder="Longitude"
                />
              </div>
            </div>
            
            <div className="form-actions">
              <button type="submit" className="submit-button">Add Facility</button>
              <button type="button" className="cancel-button" onClick={() => setShowForm(false)}>Cancel</button>
            </div>
          </form>
        </div>
      )}
      
      {loading ? (
        <div className="loading">Loading facilities...</div>
      ) : (
        <div className="facilities-list">
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Location</th>
                <th>Coordinates</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {facilities.map(facility => (
                <tr key={facility.facility_pk}>
                  <td>{facility.name}</td>
                  <td>{facility.description}</td>
                  <td>{facility.city}, {facility.country}</td>
                  <td>
                    {facility.latitude}, {facility.longitude}
                  </td>
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

export default Facilities;
