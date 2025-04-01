import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [isLoading, setIsLoading] = useState(true);
  const [apiStatus, setApiStatus] = useState(null);

  useEffect(() => {
    // Check API health when component mounts
    const checkApiHealth = async () => {
      try {
        const response = await fetch('http://localhost:8000/health');
        const data = await response.json();
        setApiStatus(data.status);
      } catch (error) {
        console.error('Error checking API health:', error);
        setApiStatus('unavailable');
      } finally {
        setIsLoading(false);
      }
    };

    checkApiHealth();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>OpenFootprint</h1>
        <h2>CSRD Compliance Reporting</h2>
        
        <div className="api-status">
          {isLoading ? (
            <p>Checking API status...</p>
          ) : (
            <p>API Status: <span className={apiStatus === 'healthy' ? 'status-ok' : 'status-error'}>
              {apiStatus || 'unavailable'}
            </span></p>
          )}
        </div>
        
        <div className="dashboard-preview">
          <h3>Dashboard Preview</h3>
          <p>The OpenFootprint dashboard will provide tools for:</p>
          <ul>
            <li>Emissions tracking and reporting</li>
            <li>Organizational structure management</li>
            <li>Facility-level emissions monitoring</li>
            <li>CSRD compliance verification</li>
            <li>Data quality assessment</li>
          </ul>
        </div>
      </header>
    </div>
  );
}

export default App;
