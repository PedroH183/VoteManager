# Voting Session API

A modern voting session management API built with FastAPI, SQLAlchemy, and PostgreSQL. This system allows users to create voting topics, manage voting sessions, and cast votes in a secure and organized manner.

## Architecture

This project follows Clean Architecture principles with clear separation of concerns:

```
├── app/
│   ├── api/                    # API layer (FastAPI routes)
│   │   ├── routers/           # Route handlers
│   │   └── schemas/           # Pydantic models
│   ├── application/           # Application layer
│   │   └── protocols/         # Repository interfaces
│   ├── domain/               # Domain layer
│   │   ├── entities/         # Domain entities
│   │   └── services/         # Business logic
│   └── infra/                # Infrastructure layer
│       ├── auth/             # Authentication logic
│       └── db/               # Database models & repositories
```

## Technology Stack

- **Framework**: FastAPI 0.115.13
- **Database**: PostgreSQL with AsyncPG
- **ORM**: SQLAlchemy 2.0.41 (Async)
- **Authentication**: JWT with PassLib
- **Migrations**: Alembic 1.16.2
- **Validation**: Pydantic 2.11.7
- **Server**: Uvicorn 0.34.3

## Prerequisites

- Python 3.10+
- PostgreSQL database
- Docker (optional)

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/PedroH183/VoteManager/tree/feat-sessions
cd VoteManager/backend
```

### 2. Installation

#### Using Docker

```bash
# Build and run with Docker
docker compose up 
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **Health Check**: `http://localhost:8000/api/health`


## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `POSTGRES_DB` | Database name | - |
| `POSTGRES_HOST` | Database host | - |
| `POSTGRES_USER` | Database user | - |
| `POSTGRES_PASSWORD` | Database password | - |
| `SECRET_KEY` | JWT secret key | - |
| `ALGORITHM` | JWT algorithm | HS256 |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiration | 30 |