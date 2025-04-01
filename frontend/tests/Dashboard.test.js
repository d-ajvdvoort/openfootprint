import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { BrowserRouter } from 'react-router-dom';
import Dashboard from '../src/pages/Dashboard';

describe('Dashboard Component', () => {
  beforeEach(() => {
    // Mock setTimeout to immediately execute callbacks
    jest.useFakeTimers();
  });

  afterEach(() => {
    // Restore setTimeout to its original implementation
    jest.useRealTimers();
  });

  test('renders Dashboard title', () => {
    render(
      <BrowserRouter>
        <Dashboard />
      </BrowserRouter>
    );
    
    // Check if the page title is rendered
    expect(screen.getByText('Dashboard')).toBeInTheDocument();
  });

  test('displays loading state initially', () => {
    render(
      <BrowserRouter>
        <Dashboard />
      </BrowserRouter>
    );
    
    // Check if loading message is displayed
    expect(screen.getByText('Loading dashboard data...')).toBeInTheDocument();
  });

  test('displays dashboard content after loading', async () => {
    render(
      <BrowserRouter>
        <Dashboard />
      </BrowserRouter>
    );
    
    // Fast-forward timers to trigger the setTimeout callback
    jest.runAllTimers();
    
    // Wait for the data to load
    await waitFor(() => {
      expect(screen.queryByText('Loading dashboard data...')).not.toBeInTheDocument();
    });
    
    // Check if dashboard sections are displayed
    expect(screen.getByText('Organizations')).toBeInTheDocument();
    expect(screen.getByText('Facilities')).toBeInTheDocument();
    expect(screen.getByText('Emission Reports')).toBeInTheDocument();
    expect(screen.getByText('Emission Statements')).toBeInTheDocument();
    expect(screen.getByText('CSRD Reports')).toBeInTheDocument();
  });

  test('displays CSRD compliance status section', async () => {
    render(
      <BrowserRouter>
        <Dashboard />
      </BrowserRouter>
    );
    
    // Fast-forward timers to trigger the setTimeout callback
    jest.runAllTimers();
    
    // Wait for the data to load
    await waitFor(() => {
      expect(screen.queryByText('Loading dashboard data...')).not.toBeInTheDocument();
    });
    
    // Check if CSRD compliance status section is displayed
    expect(screen.getByText('CSRD Compliance Status')).toBeInTheDocument();
    expect(screen.getByText('75% Complete')).toBeInTheDocument();
    
    // Check if compliance categories are displayed
    expect(screen.getByText('Environmental')).toBeInTheDocument();
    expect(screen.getByText('Social')).toBeInTheDocument();
    expect(screen.getByText('Governance')).toBeInTheDocument();
    
    // Check if compliance checklist is displayed
    expect(screen.getByText('Organization structure defined')).toBeInTheDocument();
    expect(screen.getByText('Facilities registered')).toBeInTheDocument();
    expect(screen.getByText('Emission data collected')).toBeInTheDocument();
    expect(screen.getByText('ESRS compliance verification')).toBeInTheDocument();
    expect(screen.getByText('Double materiality assessment')).toBeInTheDocument();
    expect(screen.getByText('Final CSRD report generation')).toBeInTheDocument();
  });

  test('displays recent activity section', async () => {
    render(
      <BrowserRouter>
        <Dashboard />
      </BrowserRouter>
    );
    
    // Fast-forward timers to trigger the setTimeout callback
    jest.runAllTimers();
    
    // Wait for the data to load
    await waitFor(() => {
      expect(screen.queryByText('Loading dashboard data...')).not.toBeInTheDocument();
    });
    
    // Check if recent activity section is displayed
    expect(screen.getByText('Recent Activity')).toBeInTheDocument();
    expect(screen.getByText('New CSRD report created for 2024 Annual Reporting')).toBeInTheDocument();
    expect(screen.getByText('Added 3 new facilities to Manufacturing division')).toBeInTheDocument();
    expect(screen.getByText('Updated organizational structure')).toBeInTheDocument();
    expect(screen.getByText('Completed ESRS validation for 2024 annual report')).toBeInTheDocument();
  });

  test('displays CSRD reporting deadlines section', async () => {
    render(
      <BrowserRouter>
        <Dashboard />
      </BrowserRouter>
    );
    
    // Fast-forward timers to trigger the setTimeout callback
    jest.runAllTimers();
    
    // Wait for the data to load
    await waitFor(() => {
      expect(screen.queryByText('Loading dashboard data...')).not.toBeInTheDocument();
    });
    
    // Check if CSRD reporting deadlines section is displayed
    expect(screen.getByText('CSRD Reporting Deadlines')).toBeInTheDocument();
    expect(screen.getByText('Annual CSRD Report')).toBeInTheDocument();
    expect(screen.getByText('June 30, 2025')).toBeInTheDocument();
    expect(screen.getByText('45% Complete')).toBeInTheDocument();
    expect(screen.getByText('Q1 2025 Interim Report')).toBeInTheDocument();
    expect(screen.getByText('May 15, 2025')).toBeInTheDocument();
    expect(screen.getByText('20% Complete')).toBeInTheDocument();
  });
});
