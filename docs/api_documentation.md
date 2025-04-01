# OpenFootprint API Documentation

## Overview

The OpenFootprint API provides programmatic access to CSRD compliance reporting functionality. This RESTful API allows developers to integrate OpenFootprint with other systems, automate reporting processes, and build custom interfaces.

## Base URL

```
https://your-instance.openfootprint.org/api
```

Replace `your-instance.openfootprint.org` with your actual OpenFootprint instance domain.

## Authentication

All API requests require authentication using JSON Web Tokens (JWT). To authenticate:

1. Obtain a token by sending a POST request to `/api/auth/token` with your credentials
2. Include the token in the Authorization header of all subsequent requests:
   ```
   Authorization: Bearer YOUR_TOKEN
   ```

## API Endpoints

### Organizations

#### Get All Organizations

```
GET /api/organizations/
```

**Query Parameters:**
- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

**Response:**
```json
[
  {
    "organization_pk": "namespace:master-data--Organization:12345",
    "name": "Example Corporation",
    "description": "Parent company",
    "parent_organization_id": null
  },
  {
    "organization_pk": "namespace:master-data--Organization:12346",
    "name": "Manufacturing Division",
    "description": "Manufacturing operations",
    "parent_organization_id": "namespace:master-data--Organization:12345"
  }
]
```

#### Get Organization by ID

```
GET /api/organizations/{organization_pk}
```

**Response:**
```json
{
  "organization_pk": "namespace:master-data--Organization:12345",
  "name": "Example Corporation",
  "description": "Parent company",
  "parent_organization_id": null
}
```

#### Create Organization

```
POST /api/organizations/
```

**Request Body:**
```json
{
  "organization_pk": "namespace:master-data--Organization:12347",
  "name": "New Division",
  "description": "New business division",
  "parent_organization_id": "namespace:master-data--Organization:12345"
}
```

**Response:**
```json
{
  "organization_pk": "namespace:master-data--Organization:12347",
  "name": "New Division",
  "description": "New business division",
  "parent_organization_id": "namespace:master-data--Organization:12345"
}
```

### Facilities

#### Get All Facilities

```
GET /api/facilities/
```

**Query Parameters:**
- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

**Response:**
```json
[
  {
    "facility_pk": "namespace:master-data--Facility:12345",
    "name": "Headquarters",
    "description": "Corporate headquarters",
    "address": "123 Main Street",
    "city": "New York",
    "country": "USA",
    "latitude": 40.7128,
    "longitude": -74.0060
  }
]
```

#### Get Facility by ID

```
GET /api/facilities/{facility_pk}
```

**Response:**
```json
{
  "facility_pk": "namespace:master-data--Facility:12345",
  "name": "Headquarters",
  "description": "Corporate headquarters",
  "address": "123 Main Street",
  "city": "New York",
  "country": "USA",
  "latitude": 40.7128,
  "longitude": -74.0060
}
```

#### Create Facility

```
POST /api/facilities/
```

**Request Body:**
```json
{
  "facility_pk": "namespace:master-data--Facility:12346",
  "name": "Manufacturing Plant",
  "description": "Main manufacturing facility",
  "address": "456 Industrial Blvd",
  "city": "Chicago",
  "country": "USA",
  "latitude": 41.8781,
  "longitude": -87.6298
}
```

**Response:**
```json
{
  "facility_pk": "namespace:master-data--Facility:12346",
  "name": "Manufacturing Plant",
  "description": "Main manufacturing facility",
  "address": "456 Industrial Blvd",
  "city": "Chicago",
  "country": "USA",
  "latitude": 41.8781,
  "longitude": -87.6298
}
```

### Emission Reports

#### Get All Emission Reports

```
GET /api/emission-reports/
```

**Query Parameters:**
- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

**Response:**
```json
[
  {
    "emission_report_pk": "namespace:transactional-data--EmissionReport:12345",
    "description": "Annual GHG emissions report for 2024",
    "report_period_start": "2024-01-01T00:00:00Z",
    "report_period_end": "2024-12-31T23:59:59Z",
    "organization_id": "namespace:master-data--Organization:12345",
    "report_type": "CSRD",
    "status": "Draft"
  }
]
```

#### Get Emission Report by ID

```
GET /api/emission-reports/{emission_report_pk}
```

**Response:**
```json
{
  "emission_report_pk": "namespace:transactional-data--EmissionReport:12345",
  "description": "Annual GHG emissions report for 2024",
  "report_period_start": "2024-01-01T00:00:00Z",
  "report_period_end": "2024-12-31T23:59:59Z",
  "organization_id": "namespace:master-data--Organization:12345",
  "report_type": "CSRD",
  "status": "Draft"
}
```

#### Create Emission Report

```
POST /api/emission-reports/
```

**Request Body:**
```json
{
  "emission_report_pk": "namespace:transactional-data--EmissionReport:12346",
  "description": "Q1 2025 emissions report",
  "report_period_start": "2025-01-01T00:00:00Z",
  "report_period_end": "2025-03-31T23:59:59Z",
  "organization_id": "namespace:master-data--Organization:12345",
  "report_type": "CSRD",
  "status": "Draft"
}
```

**Response:**
```json
{
  "emission_report_pk": "namespace:transactional-data--EmissionReport:12346",
  "description": "Q1 2025 emissions report",
  "report_period_start": "2025-01-01T00:00:00Z",
  "report_period_end": "2025-03-31T23:59:59Z",
  "organization_id": "namespace:master-data--Organization:12345",
  "report_type": "CSRD",
  "status": "Draft"
}
```

### CSRD Reports

#### Get All CSRD Reports

```
GET /api/csrd-reports/
```

**Query Parameters:**
- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

**Response:**
```json
[
  {
    "csrd_report_pk": "namespace:transactional-data--CSRDReport:12345",
    "title": "Annual CSRD Compliance Report 2024",
    "description": "Comprehensive sustainability report following CSRD requirements",
    "reporting_period_start": "2024-01-01T00:00:00Z",
    "reporting_period_end": "2024-12-31T23:59:59Z",
    "organization_id": "namespace:master-data--Organization:12345",
    "report_type": "Annual",
    "status": "Draft",
    "version": "1.0",
    "prepared_by": "Sustainability Department",
    "approved_by": null,
    "emission_report_ids": [
      "namespace:transactional-data--EmissionReport:12345",
      "namespace:transactional-data--EmissionReport:12346"
    ],
    "created_at": "2025-04-01T00:00:00Z",
    "updated_at": null
  }
]
```

#### Get CSRD Report by ID

```
GET /api/csrd-reports/{csrd_report_pk}
```

**Response:**
```json
{
  "csrd_report_pk": "namespace:transactional-data--CSRDReport:12345",
  "title": "Annual CSRD Compliance Report 2024",
  "description": "Comprehensive sustainability report following CSRD requirements",
  "reporting_period_start": "2024-01-01T00:00:00Z",
  "reporting_period_end": "2024-12-31T23:59:59Z",
  "organization_id": "namespace:master-data--Organization:12345",
  "report_type": "Annual",
  "status": "Draft",
  "version": "1.0",
  "prepared_by": "Sustainability Department",
  "approved_by": null,
  "emission_report_ids": [
    "namespace:transactional-data--EmissionReport:12345",
    "namespace:transactional-data--EmissionReport:12346"
  ],
  "created_at": "2025-04-01T00:00:00Z",
  "updated_at": null
}
```

#### Create CSRD Report

```
POST /api/csrd-reports/
```

**Request Body:**
```json
{
  "csrd_report_pk": "namespace:transactional-data--CSRDReport:12346",
  "title": "Q1 2025 CSRD Report",
  "description": "Quarterly sustainability report",
  "reporting_period_start": "2025-01-01T00:00:00Z",
  "reporting_period_end": "2025-03-31T23:59:59Z",
  "organization_id": "namespace:master-data--Organization:12345",
  "report_type": "Interim",
  "status": "Draft",
  "version": "1.0",
  "prepared_by": "Sustainability Department",
  "approved_by": null,
  "emission_report_ids": [
    "namespace:transactional-data--EmissionReport:12346"
  ]
}
```

**Response:**
```json
{
  "csrd_report_pk": "namespace:transactional-data--CSRDReport:12346",
  "title": "Q1 2025 CSRD Report",
  "description": "Quarterly sustainability report",
  "reporting_period_start": "2025-01-01T00:00:00Z",
  "reporting_period_end": "2025-03-31T23:59:59Z",
  "organization_id": "namespace:master-data--Organization:12345",
  "report_type": "Interim",
  "status": "Draft",
  "version": "1.0",
  "prepared_by": "Sustainability Department",
  "approved_by": null,
  "emission_report_ids": [
    "namespace:transactional-data--EmissionReport:12346"
  ],
  "created_at": "2025-04-01T00:00:00Z",
  "updated_at": null
}
```

#### Validate CSRD Report

```
GET /api/csrd-reports/{csrd_report_pk}/validate
```

**Response:**
```json
{
  "overall_status": "passed",
  "validation_date": "2025-04-01T12:34:56Z",
  "standards_version": "ESRS 2023",
  "checks": [
    {
      "standard": "ESRS E1",
      "description": "Climate change",
      "status": "passed",
      "details": "All required climate change disclosures are present"
    },
    {
      "standard": "ESRS E2",
      "description": "Pollution",
      "status": "warning",
      "details": "Some pollution metrics may need additional context"
    },
    {
      "standard": "ESRS S1",
      "description": "Own workforce",
      "status": "passed",
      "details": "Workforce disclosures are complete"
    }
  ]
}
```

#### Generate CSRD Report Document

```
GET /api/csrd-reports/{csrd_report_pk}/generate?format=pdf
```

**Query Parameters:**
- `format` (optional): Document format (pdf, html, docx) (default: pdf)

**Response:**
```json
{
  "status": "success",
  "message": "CSRD report document generated in pdf format",
  "report_id": "namespace:transactional-data--CSRDReport:12345",
  "generated_at": "2025-04-01T12:34:56Z",
  "download_url": "/api/csrd-reports/namespace:transactional-data--CSRDReport:12345/download?format=pdf"
}
```

## Error Responses

The API uses standard HTTP status codes to indicate the success or failure of requests:

- `200 OK`: The request was successful
- `400 Bad Request`: The request was invalid or cannot be served
- `401 Unauthorized`: Authentication is required or failed
- `403 Forbidden`: The authenticated user does not have permission
- `404 Not Found`: The requested resource does not exist
- `500 Internal Server Error`: An error occurred on the server

Error responses include a JSON body with details:

```json
{
  "detail": "Error message describing what went wrong"
}
```

## Rate Limiting

API requests are subject to rate limiting to ensure system stability. The current limits are:

- 100 requests per minute per authenticated user
- 1000 requests per hour per authenticated user

Rate limit headers are included in all responses:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1617234567
```

## Pagination

List endpoints support pagination using `skip` and `limit` parameters. The response does not currently include pagination metadata, but future versions may include total count and links to next/previous pages.

## Versioning

The API is versioned through the URL path. The current version is v1, which is implicit in the base URL. Future versions will be explicitly versioned (e.g., `/api/v2/`).

## Support

For API support, please contact your OpenFootprint administrator or support team.
