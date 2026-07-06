# Risk Control API Platform

## Application Architecture Document

**Project:** Risk Control API Platform  
**Project Number:** 8  
**Document Type:** Application Architecture  
**Architecture Style:** Modular Layered Backend Architecture  
**Primary Language:** Python  
**Primary Framework:** FastAPI  
**Status:** Initial Architecture Design  

---

# 1. Document Purpose

The purpose of this document is to define the high-level application architecture for the Risk Control API Platform.

The architecture translates the project's business, functional, non-functional, and technical requirements into a structured backend application design.

This document defines:

- The high-level system architecture
- The request and response lifecycle
- Application layers and responsibilities
- Separation of concerns
- Database interaction strategy
- Local and future-state database technologies
- Key architectural decisions and tradeoffs

---

# 2. Architecture Overview

The Risk Control API Platform will use a modular layered backend architecture.

The architecture separates application responsibilities into logical components responsible for:

- Receiving HTTP requests
- Routing application operations
- Validating incoming data
- Applying business rules
- Managing data access
- Mapping Python objects to relational database records
- Persisting application data
- Validating outgoing responses
- Returning HTTP responses to clients

The architecture is designed to improve:

- Maintainability
- Testability
- Readability
- Modularity
- Scalability
- Data integrity
- Future application expansion

---

# 3. High-Level Architecture

The application will use the following request and response flow:

    CLIENT
       │
       │ HTTP Request + JSON
       ▼
    FASTAPI ROUTE
       │
       │ Receives and directs request
       ▼
    PYDANTIC REQUEST SCHEMA
       │
       │ Validates incoming data
       ▼
    SERVICE LAYER
       │
       │ Applies business rules
       ▼
    DATA ACCESS LAYER
       │
       │ Performs database operations
       ▼
    SQLALCHEMY ORM
       │
       │ Maps Python objects to database records
       ▼
    RELATIONAL DATABASE
       │
       │ Stores and retrieves application data
       ▼
    SQLALCHEMY ORM
       │
       │ Returns stored database record
       ▼
    DATA ACCESS LAYER
       │
       │ Returns database result
       ▼
    SERVICE LAYER
       │
       │ Completes business operation
       ▼
    PYDANTIC RESPONSE SCHEMA
       │
       │ Validates and controls outgoing data
       ▼
    FASTAPI ROUTE
       │
       │ Returns HTTP response
       ▼
    CLIENT

---

# 4. Example Request Lifecycle

The initial architecture was designed using the following business scenario:

> A Risk & Controls Analyst wants to create a new control record.

The client submits control information to the application:

    POST /controls

The request contains JSON data representing the proposed control.

Example:

    {
      "control_name": "User Access Review",
      "control_owner": "Technology Risk",
      "frequency": "Quarterly",
      "status": "Active"
    }

The application processes the request through the following lifecycle.

## Step 1 — Client Request

A client sends an HTTP POST request containing control information.

Potential clients may include:

- Web applications
- Frontend applications
- Python automation scripts
- Dashboards
- Mobile applications
- Other backend systems
- API testing tools

## Step 2 — FastAPI Route

The FastAPI route acts as the controlled entry point into the backend application.

The route:

- Receives the HTTP request
- Identifies the requested operation
- Directs the request to the appropriate application components
- Returns the final HTTP response

## Step 3 — Pydantic Request Validation

The Pydantic request schema validates incoming data.

Validation may include:

- Required fields
- Data types
- Accepted values
- Data structure

Invalid requests are rejected before reaching core business logic or database operations.

## Step 4 — Service Layer

The Service Layer applies application business rules and determines whether the requested operation should be performed.

For example, the Service Layer may determine:

- Whether a duplicate control exists
- Whether the requested operation is permitted
- Whether related records meet defined business rules
- What action should occur next

## Step 5 — Data Access Layer

The Data Access Layer manages communication between application business logic and stored data.

Responsibilities include:

- Querying existing records
- Creating new records
- Retrieving records
- Updating records
- Managing database operations

## Step 6 — SQLAlchemy ORM

SQLAlchemy provides Object-Relational Mapping between Python application objects and relational database records.

SQLAlchemy allows the application to interact with relational databases using structured Python models and database sessions.

## Step 7 — Relational Database

The relational database provides persistent application storage.

The initial local development environment will use SQLite.

The architecture will support future migration to PostgreSQL for a production-capable database environment.

## Step 8 — Response Processing

After the requested database operation is completed, the resulting information travels back through the application.

The Service Layer completes the business operation.

A Pydantic response schema validates and controls the information returned to the client.

## Step 9 — HTTP Response

FastAPI returns the final HTTP response.

A successful control creation operation will return:

    201 Created

The response will contain JSON representing the created control.

---

# 5. Application Layers and Responsibilities

| Application Layer | Primary Responsibility | Question Answered |
|---|---|---|
| Client | Initiates application interaction | What does the user or system want to do? |
| FastAPI Route | Receives and directs HTTP requests | Where should this request go? |
| Pydantic Schema | Validates application data | Is the submitted data valid? |
| Service Layer | Applies business rules | Should the application perform this operation? |
| Data Access Layer | Manages database operations | How do we retrieve or store the data? |
| SQLAlchemy ORM | Maps application objects to database structures | How does Python communicate with the relational database? |
| Database | Provides persistent storage | Where is application data stored? |
| Response Schema | Controls outgoing data | What information should the client receive? |

---

# 6. Separation of Concerns

A primary architectural principle of the Risk Control API Platform is Separation of Concerns.

Separation of Concerns means that different application components are responsible for different areas of application behavior.

For example:

- Routes manage HTTP communication.
- Schemas manage data validation.
- Services manage business logic.
- The Data Access Layer manages database operations.
- ORM models represent database structures.
- Database components manage connections and sessions.

This approach prevents individual application components from becoming responsible for unrelated functionality.

Benefits include:

- Improved maintainability
- Improved testability
- Reduced code duplication
- Easier troubleshooting
- Clearer application structure
- Easier future expansion

---

# 7. Business Logic and Data Validation

The architecture distinguishes between data validation and business logic.

## Data Validation

Pydantic schemas answer:

> Is the submitted information structurally valid?

Examples include:

- Are required fields present?
- Are values using the expected data types?
- Are submitted values within accepted ranges?

## Business Logic

The Service Layer answers:

> Should the application perform the requested operation?

Examples include:

- Does the requested control already exist?
- Is the operation permitted by documented business rules?
- Does a referenced record exist?
- Should the operation proceed?

This distinction allows structural data validation and application decision-making to remain logically separated.

---

# 8. Data Access Strategy

Database operations will be separated from core business logic through a Data Access Layer.

The Service Layer will request data operations without directly managing database implementation details.

Example:

    SERVICE LAYER

    "Check whether an active control
    with this name and owner exists."

            ↓

    DATA ACCESS LAYER

    "Query the database for matching records."

            ↓

    DATABASE

    "Return matching result."

            ↓

    DATA ACCESS LAYER

            ↓

    SERVICE LAYER

    "Evaluate result and determine next action."

This approach reduces coupling between application business logic and database implementation.

---

# 9. Database Strategy

## Local Development

SQLite will be used during initial application development.

SQLite provides:

- Lightweight local data storage
- Minimal configuration
- Simple development setup
- Relational database capabilities
- Support for initial application testing

## Future-State Database

PostgreSQL will be introduced as a production-capable relational database technology.

PostgreSQL provides:

- Multi-user database capabilities
- Advanced relational database functionality
- Production-capable persistence
- Scalability for future application growth

## Database Abstraction

SQLAlchemy will provide the primary Object-Relational Mapping layer between the Python application and relational database technology.

The application architecture will minimize unnecessary database-specific coupling where appropriate.

---

# 10. Architectural Decision: Soft Deactivation

Control records will use logical deactivation rather than immediate permanent deletion.

Instead of permanently removing a control:

    ACTIVE CONTROL
          ↓
      DEACTIVATE
          ↓
    INACTIVE CONTROL
          ↓
    HISTORICAL RECORD PRESERVED

This decision supports:

- Historical traceability
- Audit requirements
- Record retention
- Data integrity

---

# 11. Architectural Decision: Duplicate Control Handling

The initial application design will treat an active control with the same control name and control owner as a potential duplicate.

The application will:

1. Validate incoming control data.
2. Query existing control records.
3. Determine whether a matching active control exists.
4. Reject confirmed duplicate creation attempts.
5. Return an appropriate HTTP response.

The expected duplicate response will be:

    409 Conflict

This business rule may be refined as project requirements evolve.

---

# 12. Architectural Decision: Controlled Responses

Database records will not automatically be returned directly to clients.

Pydantic response schemas will define the application data contract for outgoing responses.

This approach allows the application to:

- Control exposed information
- Validate outgoing data
- Maintain consistent response structures
- Prevent unnecessary internal fields from being returned
- Support future API evolution

---

# 13. Key Architectural Tradeoffs

## Layered Architecture

**Decision:**  
Use separated routes, schemas, services, data access components, ORM models, and database components.

**Benefit:**  
Improves maintainability, testability, readability, and separation of responsibilities.

**Tradeoff:**  
Introduces more application structure and files than a simplified backend design.

## SQLite for Initial Development

**Decision:**  
Use SQLite during initial local application development.

**Benefit:**  
Reduces setup complexity and allows development to begin with lightweight relational persistence.

**Tradeoff:**  
SQLite does not provide all capabilities expected from a production-scale multi-user database.

## PostgreSQL Future State

**Decision:**  
Design the application to support future PostgreSQL migration.

**Benefit:**  
Provides a path toward production-capable relational persistence.

**Tradeoff:**  
Database migration may require additional configuration, testing, and database-specific considerations.

## Soft Deactivation

**Decision:**  
Deactivate control records rather than immediately deleting them.

**Benefit:**  
Preserves historical traceability and supports audit-related use cases.

**Tradeoff:**  
Queries and business logic must account for active and inactive records.

---

# 14. Proposed Application Structure

Based on the architectural responsibilities defined in this document, the application will eventually use a structure similar to:

    app/
    ├── routes/
    ├── schemas/
    ├── services/
    ├── repositories/
    ├── models/
    └── database/

Each directory represents an architectural responsibility identified during system design.

The directory structure will be created incrementally as application development begins.

---

# 15. Next Steps

The next project activities will include:

1. Establish the initial application directory structure.
2. Create the FastAPI application entry point.
3. Install and document initial project dependencies.
4. Run the first local FastAPI application.
5. Implement the initial Control resource.
6. Create Control request and response schemas.
7. Develop Control business logic.
8. Implement Control data access operations.
9. Create the initial relational database model.
10. Develop automated tests.