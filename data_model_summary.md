# OpenFootprint Data Model Summary

## Overview
The provided JSON files define a comprehensive data model for CSRD (Corporate Sustainability Reporting Directive) compliance reporting, focusing on environmental footprint tracking, organizational structure, and emissions reporting. The model appears to follow ISO standards, particularly ISO 14064-1 for greenhouse gas emissions.

## Key Entities and Relationships

### Common Entities
- **Emission Statement**: Core entity representing quantification of emissions released or removed from the atmosphere
- Contains relationships to Emission Activities and Emission Calculation Models
- Follows ISO 14064-1 standards but not limited to GHG emissions

### Reporting
- **Emission Report**: Documents that describe an organization's emission inventory over a period
- Follows ISO 14064-1 GHG Report Content standards
- Contains descriptive information and primary keys for identification

### Recording
- **Emission Argument Value**: Stores values related to emission calculations
- Contains primary keys and relationships to other entities

### Organizational Structure
- References external definitions for Emission Statements
- Defines relationships between organizational entities and emissions

### Organizational Boundary
- Defines **Organization** entities as legal or administrative bodies
- References external definitions for organizational structures

### Facility Structure
- References Emission Statements in the context of facilities
- Establishes relationships between facilities and emissions

### Product Life Cycle
- **Environmental Product Declaration**: Documents containing information about products' potential environmental and human health impacts
- Follows ISO 14040 series standards for Type III environmental declarations

### Data Verification
- **DataQuality**: Entities for verifying and ensuring quality of emissions data
- Contains identification and relationship information

### Water and Waste
- **Water Activity Type**: Categorizes water-related activities
- Contains identification and naming information

## Cross-cutting Patterns
- Consistent use of primary keys with specific patterns
- External references between models
- ISO standard compliance throughout
- Clear separation of concerns between organizational structure, emissions recording, and reporting

This data model provides a foundation for building a CSRD compliance reporting system that can track, calculate, verify, and report on environmental impacts across an organization's structure, facilities, and products.
