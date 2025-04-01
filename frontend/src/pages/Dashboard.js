import React, { useState, useEffect } from 'react';
import './Dashboard.css';

const Dashboard = () => {
  const [stats, setStats] = useState({
    organizations: 0,
    facilities: 0,
    emissionReports: 0,
    emissionStatements: 0,
    csrdReports: 0
  });
  
  const [loading, setLoading] = useState(true);
  const [csrdCompliance, setCSRDCompliance] = useState({
    overall: 75,
    categories: [
      { name: 'Environmental', score: 82, color: '#4CAF50' },
      { name: 'Social', score: 68, color: '#FFC107' },
      { name: 'Governance', score: 76, color: '#2196F3' }
    ]
  });

  useEffect(() => {
    // In a real implementation, this would fetch data from the API
    // Simulating API call with setTimeout
    setTimeout(() => {
      setStats({
        organizations: 5,
        facilities: 12,
        emissionReports: 8,
        emissionStatements: 124,
        csrdReports: 2
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
            <div className="stat-card highlight">
              <h3>CSRD Reports</h3>
              <p className="stat-value">{stats.csrdReports}</p>
            </div>
          </div>
          
          <div className="dashboard-section">
            <h2>CSRD Compliance Status</h2>
            <div className="compliance-status">
              <div className="progress-bar">
                <div className="progress" style={{ width: `${csrdCompliance.overall}%` }}></div>
              </div>
              <p>{csrdCompliance.overall}% Complete</p>
            </div>
            
            <div className="compliance-categories">
              {csrdCompliance.categories.map((category, index) => (
                <div key={index} className="compliance-category">
                  <h4>{category.name}</h4>
                  <div className="category-progress-bar">
                    <div 
                      className="category-progress" 
                      style={{ 
                        width: `${category.score}%`,
                        backgroundColor: category.color
                      }}
                    ></div>
                  </div>
                  <p>{category.score}%</p>
                </div>
              ))}
            </div>
            
            <ul className="compliance-checklist">
              <li className="complete">Organization structure defined</li>
              <li className="complete">Facilities registered</li>
              <li className="complete">Emission data collected</li>
              <li className="in-progress">ESRS compliance verification</li>
              <li className="in-progress">Double materiality assessment</li>
              <li className="pending">Final CSRD report generation</li>
            </ul>
          </div>
          
          <div className="dashboard-section">
            <h2>Recent Activity</h2>
            <ul className="activity-list">
              <li>
                <span className="activity-date">2025-03-28</span>
                <span className="activity-description">New CSRD report created for 2024 Annual Reporting</span>
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
                <span className="activity-description">Completed ESRS validation for 2024 annual report</span>
              </li>
            </ul>
          </div>
          
          <div className="dashboard-section">
            <h2>CSRD Reporting Deadlines</h2>
            <div className="deadlines-container">
              <div className="deadline-card">
                <div className="deadline-header">
                  <h3>Annual CSRD Report</h3>
                  <span className="deadline-date">June 30, 2025</span>
                </div>
                <div className="deadline-progress">
                  <div className="deadline-progress-bar">
                    <div className="deadline-progress-fill" style={{ width: '45%' }}></div>
                  </div>
                  <span className="deadline-progress-text">45% Complete</span>
                </div>
                <div className="deadline-actions">
                  <button className="deadline-action-button">View Report</button>
                </div>
              </div>
              
              <div className="deadline-card">
                <div className="deadline-header">
                  <h3>Q1 2025 Interim Report</h3>
                  <span className="deadline-date">May 15, 2025</span>
                </div>
                <div className="deadline-progress">
                  <div className="deadline-progress-bar">
                    <div className="deadline-progress-fill" style={{ width: '20%' }}></div>
                  </div>
                  <span className="deadline-progress-text">20% Complete</span>
                </div>
                <div className="deadline-actions">
                  <button className="deadline-action-button">View Report</button>
                </div>
              </div>
            </div>
          </div>
        </>
      )}
    </div>
  );
};

export default Dashboard;
