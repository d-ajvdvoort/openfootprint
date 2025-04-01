import React from 'react';
import { HashRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';
import Dashboard from './pages/Dashboard';
import Organizations from './pages/Organizations';
import Facilities from './pages/Facilities';
import EmissionReports from './pages/EmissionReports';
import EmissionStatements from './pages/EmissionStatements';
import CSRDReports from './pages/CSRDReports';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>OpenFootprint</h1>
          <h2>CSRD Compliance Reporting</h2>
          <nav className="main-nav">
            <ul>
              <li><Link to="/">Dashboard</Link></li>
              <li><Link to="/organizations">Organizations</Link></li>
              <li><Link to="/facilities">Facilities</Link></li>
              <li><Link to="/emission-reports">Emission Reports</Link></li>
              <li><Link to="/emission-statements">Emission Statements</Link></li>
              <li><Link to="/csrd-reports">CSRD Reports</Link></li>
            </ul>
          </nav>
        </header>
        <main className="App-content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/organizations" element={<Organizations />} />
            <Route path="/facilities" element={<Facilities />} />
            <Route path="/emission-reports" element={<EmissionReports />} />
            <Route path="/emission-statements" element={<EmissionStatements />} />
            <Route path="/csrd-reports" element={<CSRDReports />} />
          </Routes>
        </main>
        <footer className="App-footer">
          <p>OpenFootprint - CSRD Compliance Reporting © 2025</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
