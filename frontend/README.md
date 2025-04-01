# Frontend Setup for OpenFootprint

This directory contains the React frontend for the OpenFootprint application.

## Structure

- `src/`: Source code
  - `components/`: Reusable UI components
  - `pages/`: Application pages
  - `services/`: API service calls
  - `context/`: React context providers
  - `hooks/`: Custom React hooks
  - `utils/`: Utility functions
  - `assets/`: Static assets
- `public/`: Public assets

## Setup

1. Install dependencies:
```
npm install
```

2. Set up environment variables:
```
cp .env.example .env.local
# Edit .env.local with your configuration
```

3. Start the development server:
```
npm start
```

4. Build for production:
```
npm run build
```
