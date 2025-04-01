import React, { useState, useEffect } from 'react';
import './Dashboard.css';

const Dashboard = () => {
  const [stats, setStats] = useState({
    organizations: 0,
    facilities: 0,
    emissionReports: 0,
    emissionStatements: 0
  });
  
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // In a real implementation, this would fetch data from the API
    // Simulating API call with setTimeout
    setTimeout(() => {
      setStats({
        organizations: 5,
        facilities: 12,
        emissionReports: 8,
        emissionStatements: 124
      });
      setLoading(false);
    }, 1000);
  }, []);

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      
      {loading ? (
        <div className="loading">Loading dashboard data...</div>
      ) : (
        <>
          <div className="stats-container">
            <div className="stat-card">
              <h3>Organizations</h3>
              <p className="stat-value">{stats.organizations}</p>
            </div>
            <div className="stat-card">
              <h3>Facilities</h3>
              <p className="stat-value">{stats.facilities}</p>
            </div>
            <div className="stat-card">
              <h3>Emission Reports</h3>
              <p className="stat-value">{stats.emissionReports}</p>
            </div>
            <div className="stat-card">
              <h3>Emission Statements</h3>
              <p className="stat-value">{stats.emissionStatements}</p>
            </div>
          </div>
          
          <div className="dashboard-section">
            <h2>CSRD Compliance Status</h2>
            <div className="compliance-status">
              <div className="progress-bar">
                <div className="progress" style={{ width: '75%' }}></div>
              </div>
              <p>75% Complete</p>
            </div>
            <ul className="compliance-checklist">
              <li className="complete">Organization structure defined</li>
              <li className="complete">Facilities registered</li>
              <li className="complete">Emission data collected</li>
              <li className="in-progress">Verification in progress</li>
              <li className="pending">Final report generation</li>
            </ul>
          </div>
          
          <div className="dashboard-section">
            <h2>Recent Activity</h2>
            <ul className="activity-list">
              <li>
                <span className="activity-date">2025-03-28</span>
                <span className="activity-description">New emission report created for Q1 2025</span>
              </li>
              <li>
                <span className="activity-date">2025-03-25</span>
                <span className="activity-description">Added 3 new facilities to Manufacturing division</span>
              </li>
              <li>
                <span className="activity-date">2025-03-20</span>
                <span className="activity-description">Updated organizational structure</span>
              </li>
              <li>
                <span className="activity-date">2025-03-15</span>
                <span className="activity-description">Completed data verification for 2024 annual report</span>
              </li>
            </ul>
          </div>
        </>
      )}
    </div>
  );
};

export default Dashboard;
