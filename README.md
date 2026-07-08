# 🛡️ Risk Control API Platform

An enterprise-inspired backend API platform for managing risk control records, application users, audit relationships, relational database persistence, schema migrations, large-scale datasets, and containerized application environments.

Built to demonstrate backend software engineering, REST API development, relational database architecture, data validation, database migrations, performance-oriented data generation, containerization, and professional GitHub development workflows through a modular FastAPI application.

---

## ⭐ Project Highlights

- 🐍 **Language:** Python
- ⚡ **API Framework:** FastAPI
- 🗄️ **Database:** PostgreSQL 18
- 🔗 **ORM:** SQLAlchemy
- 🔄 **Database Migrations:** Alembic
- 📋 **Data Validation:** Pydantic
- 🐳 **Containerization:** Docker & Docker Compose
- 🌐 **API Documentation:** Swagger UI / OpenAPI
- 📊 **Large-Scale Dataset:** 100,055 Control Records
- 👥 **Relational Data:** User & Control Audit Relationships
- 🔀 **Development Workflow:** Git, GitHub Issues, Feature Branches & Pull Requests
- 💼 **Focus:** Backend Software Engineering Portfolio Project

---

## 📊 Project Statistics

| Metric | Value |
|---------|------:|
| Programming Language | Python |
| API Framework | FastAPI |
| Database Platform | PostgreSQL 18 |
| ORM Framework | SQLAlchemy |
| Migration Framework | Alembic |
| Container Services | 2 |
| Standard Control Records | 55 |
| Large-Scale Generated Records | 100,000 |
| Maximum Tested Dataset | 100,055 |
| Application Users | 5 |
| Application Architecture | Layered |
| Container Architecture | Multi-Service |
| API Documentation | Swagger UI / OpenAPI |

---

# 📋 Overview

The Risk Control API Platform is an enterprise-inspired backend application designed to manage risk control records through a structured REST API.

The application supports control creation, retrieval, updating, deletion, filtering, pagination, user audit relationships, relational database persistence, schema migrations, large-scale dataset generation, and containerized application execution.

The project began as a FastAPI application using a lightweight local database architecture and evolved into a PostgreSQL-backed, multi-container application environment.

Throughout development, the platform was progressively enhanced with SQLAlchemy ORM models, Pydantic request and response schemas, Alembic database migrations, application users, foreign-key relationships, nested audit responses, pagination, filtering, large-scale data generation, Docker containerization, PostgreSQL health monitoring, persistent database storage, and service dependency management.

The completed application demonstrates how backend systems evolve through incremental engineering enhancements while maintaining structured version control and development workflows.

---

# 🎯 Business Scenario

Enterprise risk and control environments require reliable systems for storing, retrieving, updating, and monitoring control information.

Control records may contain information such as:

- Control name
- Control owner
- Execution frequency
- Operational status
- Control description
- Creation timestamp
- Modification timestamp
- Creating user
- Updating user

As the number of control records grows, manually managing this information becomes inefficient and difficult to scale.

The Risk Control API Platform addresses this problem by providing a centralized backend service that exposes structured REST API endpoints for managing control records stored within a relational PostgreSQL database.

The platform also introduces user audit relationships that allow control records to identify the users responsible for creating and updating data.

Large-scale data generation capabilities provide an additional mechanism for evaluating API behavior against datasets containing more than 100,000 records.

Docker and Docker Compose extend the application architecture by allowing the FastAPI application and PostgreSQL database to run as coordinated container services within a reproducible development environment.

---

# 🚀 Project Objectives

- Build a structured REST API using FastAPI
- Implement enterprise-inspired backend application architecture
- Manage risk control records through CRUD operations
- Validate API requests and responses using Pydantic
- Implement relational database persistence using PostgreSQL
- Manage database interactions through SQLAlchemy ORM
- Introduce version-controlled database migrations using Alembic
- Create application users and relational audit fields
- Implement foreign-key relationships between controls and users
- Return nested audit information through API responses
- Support API pagination and filtering
- Generate large-scale datasets for scalability testing
- Containerize the FastAPI application using Docker
- Coordinate application and database services using Docker Compose
- Implement PostgreSQL health monitoring and service dependencies
- Demonstrate professional GitHub development workflows
- Produce a portfolio-quality backend software engineering project

---

# 📈 Current Project Status

## ✅ Completed

- Project Planning
- Backend Application Architecture
- FastAPI Application Setup
- REST API Endpoint Development
- CRUD Operations
- Pydantic Request Validation
- Pydantic Response Serialization
- SQLAlchemy ORM Integration
- Database Session Management
- PostgreSQL 18 Integration
- Database Migration from SQLite Architecture
- Alembic Configuration
- Baseline Database Migration
- Schema Migration Management
- User Database Model
- User Seed Data
- Control Audit Fields
- Foreign-Key Relationships
- Nested User Audit Responses
- Control Filtering
- API Pagination
- Standard Demonstration Dataset
- Large-Scale Dataset Generation
- 100,055-Record API Testing
- DBeaver Database Validation
- Dockerfile Configuration
- Docker Compose Configuration
- FastAPI Containerization
- PostgreSQL Containerization
- Persistent Database Storage
- PostgreSQL Health Checks
- Service Dependency Management
- Docker Container Networking
- Containerized Database Seeding
- Containerized Large-Scale Data Generation
- Swagger UI Validation
- GitHub Issues
- Feature Branch Development
- Pull Request Reviews
- Branch Merges
- Technical Documentation
- Repository Documentation

## 🔮 Planned

- Automated Test Suite Expansion
- User Authentication
- Role-Based Access Control
- API Logging
- Advanced Search Capabilities
- Database Index Optimization
- CI/CD Pipeline
- Cloud Deployment
- API Monitoring
- Kubernetes Orchestration

---

# 🏗️ System Architecture

```text
API Client
    │
    ▼
Swagger UI / HTTP Request
    │
    ▼
FastAPI Application
    │
    ▼
API Router Layer
    │
    ▼
Pydantic Validation
    │
    ▼
SQLAlchemy ORM
    │
    ▼
PostgreSQL 18 Database
    │
    ├── Users
    │
    └── Controls
         │
         ├── created_by_id
         └── updated_by_id
```

The application follows a layered backend architecture that separates API routing, request validation, database models, relational data management, and persistence responsibilities.

FastAPI processes incoming HTTP requests and exposes interactive API documentation through Swagger UI.

Pydantic validates incoming data and serializes structured API responses.

SQLAlchemy provides the Object Relational Mapping layer between Python application objects and PostgreSQL database tables.

PostgreSQL provides persistent relational data storage, while Alembic manages version-controlled database schema changes.

---

# ⚙️ Application Workflow

1. An API client sends an HTTP request to the FastAPI application.
2. FastAPI routes the request to the appropriate API endpoint.
3. Pydantic validates incoming request data.
4. The application creates a SQLAlchemy database session.
5. SQLAlchemy translates ORM operations into database queries.
6. PostgreSQL processes the requested database operation.
7. Related user audit information is retrieved when required.
8. SQLAlchemy returns the database results to the application.
9. Pydantic serializes the response data.
10. FastAPI returns the completed JSON response to the client.

---

# 📁 Project Structure

```text
risk-control-api-platform
│
├── alembic
│   ├── versions
│   │   ├── baseline_existing_schema.py
│   │   └── add_user_audit_fields_to_controls.py
│   │
│   ├── env.py
│   ├── README
│   └── script.py.mako
│
├── app
│   ├── database
│   │   └── config.py
│   │
│   ├── models
│   │   ├── control.py
│   │   └── user.py
│   │
│   ├── routers
│   │   └── controls.py
│   │
│   ├── schemas
│   │   └── control.py
│   │
│   └── main.py
│
├── scripts
│   ├── assign_control_users.py
│   ├── seed_controls.py
│   ├── seed_large_controls.py
│   └── seed_users.py
│
├── tests
│
├── .dockerignore
├── .gitignore
├── alembic.ini
├── compose.yaml
├── Dockerfile
├── README.md
└── requirements.txt
```

---

# ✨ Core Features

## 🌐 REST API

- Structured FastAPI application
- RESTful endpoint design
- JSON request and response handling
- Automatic OpenAPI schema generation
- Interactive Swagger UI documentation
- HTTP status code handling
- Request validation
- Response serialization

## 🛠️ CRUD Operations

The platform supports structured control management operations including:

- Create new control records
- Retrieve control records
- Retrieve individual controls
- Update existing controls
- Delete control records

## 📋 Data Validation

Pydantic schemas provide structured validation for API requests and responses.

Validation capabilities include:

- Required field enforcement
- Minimum string lengths
- Maximum string lengths
- Enumeration-based frequency values
- Enumeration-based status values
- Optional field handling
- Structured API response models

## 🗄️ PostgreSQL Database

- PostgreSQL 18 relational database
- Persistent control records
- Persistent application users
- Primary key relationships
- Foreign-key relationships
- Indexed database fields
- Timestamp tracking
- Database session management

## 🔗 SQLAlchemy ORM

- Declarative database models
- Typed ORM mappings
- Database column definitions
- Foreign-key relationships
- User relationship resolution
- Database query abstraction
- Session-based transaction management

## 👥 User Audit Relationships

Control records support relational audit information through:

- `created_by_id`
- `updated_by_id`
- `created_by`
- `updated_by`

The API can return both foreign-key identifiers and nested user information.

Nested user information includes:

- User ID
- User name
- User role
- User department

This architecture demonstrates relational database modeling and structured API response serialization.

## 📄 Pagination

The API supports pagination through:

- `offset`
- `limit`

Pagination responses include:

- Current result count
- Total database record count
- Current offset
- Current result limit
- Returned control records

Pagination allows the application to efficiently retrieve manageable subsets of large datasets.

## 🔍 Filtering

The platform supports control filtering capabilities that allow API clients to retrieve records matching specific criteria.

Filtering can be combined with pagination to provide structured data retrieval across large datasets.

## 📊 Large-Scale Data Generation

The project includes a dedicated data generation script capable of inserting 100,000 additional control records.

Large-scale data generation occurs in batches of 5,000 records.

Example execution output:

```text
Inserted records 1 through 5000
Inserted records 5001 through 10000
Inserted records 10001 through 15000
...
Inserted records 95001 through 100000
```

Combined with the standard demonstration dataset, the application was tested against:

```text
100,055 total control records
```

## 🔄 Database Migrations

Alembic provides version-controlled database schema management.

Migration capabilities include:

- Baseline schema management
- Migration revision generation
- Database schema upgrades
- Database version tracking
- Controlled schema evolution

## 🐳 Docker Containerization

The FastAPI application is packaged within a Docker container.

The Docker image provides:

- Standardized Python runtime
- Application dependency installation
- Application source code packaging
- Consistent execution environment
- Reproducible application startup

## 🐳 Docker Compose

Docker Compose coordinates the complete application environment.

The environment contains:

```text
Docker Compose
│
├── FastAPI Container
│
└── PostgreSQL 18 Container
```

Docker Compose manages:

- Multi-service startup
- Container networking
- Environment configuration
- Persistent database storage
- PostgreSQL health monitoring
- Service startup dependencies

## 🩺 PostgreSQL Health Monitoring

The PostgreSQL container includes a database health check.

The FastAPI service waits until PostgreSQL reports a healthy status before attempting database connectivity.

This prevents application startup failures caused by the API attempting to connect before the database is ready.

## 💾 Persistent Storage

Docker volumes provide persistent PostgreSQL storage.

Database information remains available across container restarts unless the associated Docker volume is explicitly removed.

## 🏛️ Software Engineering

- Layered backend architecture
- Separation of concerns
- Modular application organization
- Relational database design
- Environment-based configuration
- Database migration management
- Containerized application architecture
- Reproducible development environments
- Feature-based development
- Version control
- Technical documentation

---

# 💻 Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| API Framework | FastAPI |
| Application Server | Uvicorn |
| Database | PostgreSQL 18 |
| ORM | SQLAlchemy |
| Data Validation | Pydantic |
| Database Migrations | Alembic |
| PostgreSQL Driver | Psycopg |
| Containerization | Docker |
| Multi-Container Management | Docker Compose |
| API Documentation | Swagger UI / OpenAPI |
| Database Management | DBeaver |
| Development Environment | PyCharm |
| Version Control | Git |
| Repository Management | GitHub |

---

# 🔌 API Endpoints

The application exposes REST API endpoints for managing control records.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/controls/` | Retrieve control records |
| GET | `/controls/{control_id}` | Retrieve a specific control |
| POST | `/controls/` | Create a new control |
| PUT | `/controls/{control_id}` | Update an existing control |
| DELETE | `/controls/{control_id}` | Delete a control |

Interactive API documentation is available through Swagger UI when the application is running.

```text
http://127.0.0.1:8000/docs
```

---

# 🗄️ Database Architecture

The PostgreSQL database contains relational models for users and controls.

```text
USERS
│
├── id
├── name
├── role
└── department

        │
        │ Foreign-Key Relationships
        ▼

CONTROLS
│
├── id
├── control_name
├── control_owner
├── frequency
├── status
├── description
├── created_at
├── updated_at
├── created_by_id
└── updated_by_id
```

The relationship architecture allows control records to reference the users responsible for creating and updating data.

---

# 👥 Audit Relationship Architecture

```text
Application User
        │
        ├───────────────┐
        │               │
        ▼               ▼
 created_by_id     updated_by_id
        │               │
        └───────┬───────┘
                │
                ▼
          Control Record
                │
                ▼
       Nested API Response
```

Example audit response structure:

```json
{
  "created_by_id": 1,
  "updated_by_id": 2,
  "created_by": {
    "id": 1,
    "name": "Maria Chen",
    "role": "Control Owner",
    "department": "Technology Risk"
  },
  "updated_by": {
    "id": 2,
    "name": "David Johnson",
    "role": "Risk Analyst",
    "department": "Enterprise Risk"
  }
}
```

---

# 📊 Dataset Architecture

The project supports two dataset configurations.

## Standard Demonstration Dataset

```text
5 Application Users
+
55 Control Records
=
Lightweight Demonstration Environment
```

The standard dataset provides a lightweight environment for:

- API demonstrations
- CRUD testing
- Relationship validation
- Swagger UI testing
- Local development

## Large-Scale Performance Dataset

```text
55 Standard Controls
+
100,000 Generated Controls
=
100,055 Total Records
```

The large-scale dataset provides an environment for:

- Pagination testing
- Filtering validation
- Large-dataset API behavior
- Database inspection
- Query response testing
- Backend scalability demonstrations

---

# 📈 Large-Scale API Testing

The application was validated against a PostgreSQL database containing 100,055 control records.

Example API request:

```text
GET /controls/?offset=0&limit=20
```

Example response metadata:

```json
{
  "message": "Controls retrieved successfully",
  "count": 20,
  "total": 100055,
  "offset": 0,
  "limit": 20
}
```

Additional pagination testing was performed using large offsets.

Example:

```text
GET /controls/?offset=50000&limit=20
```

The application successfully returned paginated API responses while maintaining the complete database record count.

---

# ⚡ API Response Testing

Local API response testing was performed using command-line HTTP requests.

Example:

```bash
time curl -s "http://127.0.0.1:8000/controls/?offset=0&limit=20" > /dev/null
```

Large-offset request:

```bash
time curl -s "http://127.0.0.1:8000/controls/?offset=50000&limit=20" > /dev/null
```

Filtered request:

```bash
time curl -s "http://127.0.0.1:8000/controls/?status=Active&offset=0&limit=20" > /dev/null
```

These tests were used to validate API responsiveness across standard, filtered, and large-offset database queries.

---

# 🐳 Docker Architecture

```text
Developer
    │
    ▼
docker compose up
    │
    ▼
Docker Compose
    │
    ├────────────────────────────┐
    │                            │
    ▼                            ▼
PostgreSQL Container       FastAPI Container
    │                            │
    │                            ▼
    │                         Uvicorn
    │                            │
    │                            ▼
    │                         FastAPI
    │                            │
    │                            ▼
    └────────────────────── SQLAlchemy
                                 │
                                 ▼
                            Swagger UI
```

The containerized architecture separates application execution from database infrastructure while allowing both services to communicate through Docker networking.

---

# 🔄 Docker Startup Workflow

```text
docker compose up
        │
        ▼
PostgreSQL Container Starts
        │
        ▼
PostgreSQL Health Check Runs
        │
        ▼
Database Reports Healthy
        │
        ▼
FastAPI Container Starts
        │
        ▼
Uvicorn Starts Application
        │
        ▼
FastAPI Connects to PostgreSQL
        │
        ▼
Swagger UI Becomes Available
```

This architecture prevents the API service from attempting to connect to PostgreSQL before the database is ready to accept connections.

---

# 🔀 GitHub Development Workflow

The project was developed using a feature-based Git and GitHub workflow.

```text
GitHub Issue
      │
      ▼
Feature Branch
      │
      ▼
Application Development
      │
      ▼
Local Testing
      │
      ▼
Git Status Review
      │
      ▼
Git Staging
      │
      ▼
Git Commit
      │
      ▼
Remote Push
      │
      ▼
Pull Request
      │
      ▼
Code Review
      │
      ▼
Merge to Main
      │
      ▼
Local Main Synchronization
```

Development enhancements were separated into focused branches and integrated into the primary application through pull requests.

This workflow demonstrates structured source control practices commonly used in collaborative software engineering environments.

---

# 💡 Engineering Challenges and Solutions

## PostgreSQL Migration

### Challenge

The application architecture required migration from a lightweight database configuration to PostgreSQL.

### Solution

The database configuration was updated to support PostgreSQL connectivity using SQLAlchemy and Psycopg.

Alembic was introduced to manage schema changes through version-controlled database migrations.

---

## User Relationship Resolution

### Challenge

Adding `created_by` and `updated_by` relationships required SQLAlchemy to correctly resolve the User model.

### Solution

The application model architecture and seed scripts were updated to ensure the User model was registered before SQLAlchemy configured ORM relationships.

---

## Large-Scale Dataset Generation

### Challenge

The application required a large dataset for pagination and scalability testing.

### Solution

A dedicated data generation script was developed to create 100,000 additional control records in batches of 5,000.

---

## Docker Dependency Installation

### Challenge

The original dependency manifest contained packages unrelated to the application that prevented successful Docker image construction.

### Solution

The dependency manifest was refined to contain application-specific dependencies required by the FastAPI platform.

---

## PostgreSQL 18 Container Storage

### Challenge

PostgreSQL 18 introduced container storage configuration behavior that conflicted with the original Docker volume configuration.

### Solution

The Docker Compose volume architecture was updated to support the PostgreSQL 18 container storage requirements.

---

## Container Startup Timing

### Challenge

The FastAPI container attempted to connect to PostgreSQL before the database was ready to accept connections.

### Solution

A PostgreSQL health check and Docker Compose service dependency condition were implemented.

The FastAPI container now waits for the PostgreSQL service to report a healthy status before starting.

---

# 🛠️ Skills Demonstrated

## 💻 Backend Software Engineering

- REST API development
- Layered application architecture
- Modular Python application design
- API request processing
- API response serialization
- Error handling
- Application configuration

## ⚡ FastAPI Development

- API router implementation
- HTTP endpoint development
- Query parameters
- Path parameters
- CRUD operations
- OpenAPI documentation
- Swagger UI testing

## 📋 Data Validation

- Pydantic models
- Request schemas
- Response schemas
- Enumeration validation
- Optional fields
- Nested response serialization

## 🗄️ Database Engineering

- PostgreSQL integration
- Relational database architecture
- SQLAlchemy ORM
- Database sessions
- Primary keys
- Foreign keys
- ORM relationships
- Database queries
- Persistent data storage

## 🔄 Database Migration Management

- Alembic configuration
- Baseline migrations
- Schema revisions
- Database upgrades
- Version-controlled schema management

## 👥 Relational Data Modeling

- User models
- Control models
- Audit fields
- Foreign-key relationships
- Nested relational responses

## 📊 Data Engineering

- Seed data generation
- Batch record insertion
- Large-scale dataset creation
- 100,055-record database testing
- Pagination validation
- Filtering validation

## 🐳 Containerization

- Dockerfile development
- Docker image construction
- Docker Compose
- Multi-container applications
- Container networking
- Persistent volumes
- Database health checks
- Service dependency management

## 🧪 Application Testing

- Swagger UI testing
- API endpoint validation
- Database verification
- DBeaver inspection
- Command-line HTTP testing
- Containerized application testing

## 🔀 Version Control

- Git repositories
- Feature branches
- GitHub Issues
- Structured commits
- Pull requests
- Branch merges
- Main branch synchronization

## 🏛️ Application Design

- Separation of concerns
- Maintainable project structure
- Reproducible development environments
- Environment configuration
- Technical documentation
- Enterprise-inspired software architecture

---

# ▶️ Installation

## Prerequisites

The application can be executed using either a local Python/PostgreSQL environment or Docker.

### Local Development Requirements

- Python 3.13
- PostgreSQL 18
- Git

### Containerized Development Requirements

- Git
- Docker Desktop
- Docker Compose

---

# 📥 Clone the Repository

Clone the repository:

```bash
git clone https://github.com/vcast525/risk-control-api-platform.git
```

Navigate to the project directory:

```bash
cd risk-control-api-platform
```

---

# 🐳 Running the Application with Docker Compose

Docker Compose provides the recommended method for running the complete application environment.

Build and start the containers:

```bash
docker compose up --build
```

After the initial image build, the existing application environment can be started using:

```bash
docker compose up
```

The Docker environment starts:

```text
FastAPI Application Container
+
PostgreSQL 18 Database Container
```

Once both services are running, access Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# 🩺 Verify Container Status

View running application services:

```bash
docker compose ps
```

View all application services, including stopped containers:

```bash
docker compose ps -a
```

View container logs:

```bash
docker compose logs --tail=50
```

View FastAPI container logs:

```bash
docker compose logs api --tail=100
```

---

# 📊 Loading the Standard Demonstration Dataset

Seed application users:

```bash
docker compose exec api python -m scripts.seed_users
```

Seed the standard control dataset:

```bash
docker compose exec api python -m scripts.seed_controls
```

Assign user audit relationships:

```bash
docker compose exec api python -m scripts.assign_control_users
```

The standard demonstration environment contains:

```text
5 Users
+
55 Controls
```

---

# 📈 Loading the Large-Scale Dataset

Generate 100,000 additional control records:

```bash
docker compose exec api python -m scripts.seed_large_controls
```

The completed large-scale environment contains:

```text
55 Standard Controls
+
100,000 Generated Controls
=
100,055 Total Controls
```

---

# 🧪 Testing the API

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Test the control list endpoint:

```text
GET /controls/?offset=0&limit=20
```

Expected large-scale response metadata:

```text
count: 20
total: 100055
offset: 0
limit: 20
```

Test an individual control:

```text
GET /controls/1
```

The response should include:

- Control information
- Creation timestamp
- Update timestamp
- Creating user ID
- Updating user ID
- Nested creating user information
- Nested updating user information

---

# 🛑 Stopping the Application

Stop the Docker Compose environment:

```bash
docker compose down
```

Stop the environment and remove associated Docker volumes:

```bash
docker compose down -v
```

> **Note:** Removing Docker volumes deletes the PostgreSQL data stored within the containerized environment.

---

# 🔮 Future Enhancements

- Automated unit testing expansion
- Integration testing
- User authentication
- JSON Web Token authentication
- Role-Based Access Control
- Advanced API search
- Dynamic sorting
- Additional filtering capabilities
- Database index optimization
- Structured application logging
- API monitoring
- Error tracking
- CI/CD pipeline
- Cloud application deployment
- Managed cloud PostgreSQL integration
- Kubernetes orchestration
- Automated container deployment
- Production environment configuration

---

# 📄 Disclaimer

This project was created for educational and software engineering portfolio demonstration purposes.

The Risk Control API Platform uses simulated users, controls, departments, roles, and organizational data. No proprietary, confidential, or production information from any financial institution or employer is included in this repository.

The project demonstrates backend software engineering, REST API development, relational database architecture, database migrations, large-scale data generation, containerization, and professional software development workflows.