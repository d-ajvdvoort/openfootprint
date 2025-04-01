# OpenFootprint Render Deployment Guide

This document provides instructions for deploying the OpenFootprint application to Render's free tier.

## Prerequisites

1. A Render account (sign up at https://render.com)
2. Access to the OpenFootprint GitHub repository

## Deployment Steps

### 1. Fork or Clone the Repository

First, ensure you have access to the OpenFootprint repository:
```
git clone https://github.com/d-ajvdvoort/openfootprint.git
cd openfootprint
```

### 2. Deploy to Render

There are two ways to deploy to Render:

#### Option A: Using the Render Dashboard

1. Log in to your Render account
2. Click "New" and select "Blueprint"
3. Connect your GitHub account if you haven't already
4. Select the OpenFootprint repository
5. Render will automatically detect the `render.yaml` file and set up the services
6. Click "Apply" to start the deployment

#### Option B: Using the Render CLI

1. Install the Render CLI:
   ```
   npm install -g @render/cli
   ```

2. Log in to your Render account:
   ```
   render login
   ```

3. Deploy the blueprint:
   ```
   render blueprint apply
   ```

### 3. Monitor Deployment

1. Render will create three services:
   - openfootprint-backend (Web Service)
   - openfootprint-frontend (Static Site)
   - openfootprint-db (PostgreSQL Database)

2. The initial deployment may take 5-10 minutes to complete

3. Once deployed, you can access your application at:
   - Frontend: https://openfootprint-frontend.onrender.com
   - Backend API: https://openfootprint-backend.onrender.com

## Important Notes

1. **Free Tier Limitations**: The backend service will spin down after 15 minutes of inactivity. The first request after inactivity may take up to 30 seconds to respond as the service spins up.

2. **Database**: The free PostgreSQL instance has a 1GB storage limit.

3. **Custom Domains**: Custom domains are not available on the free tier. If you need a custom domain, you'll need to upgrade to a paid plan.

## Troubleshooting

If you encounter issues during deployment:

1. Check the build logs in the Render dashboard
2. Ensure all environment variables are correctly set
3. Verify that the database connection is working properly
4. Check that the frontend is correctly configured to communicate with the backend API

For more detailed troubleshooting, refer to Render's documentation at https://render.com/docs
