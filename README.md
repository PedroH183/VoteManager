# VoteManager

A modern full-stack voting session management system built with React + TypeScript frontend and FastAPI backend. This application allows users to create voting topics, manage voting sessions, and cast votes in a secure and organized manner.

![alt text](image.png)

### Backend (FastAPI)
Follows Clean Architecture principles with clear separation of concerns:

```
backend/
├── app/
│   ├── api/                    # API layer (FastAPI routes)
│   │   ├── routers/           # Route handlers
│   │   ├── schemas/           # Pydantic models
│   │   └── deps.py            # Dependencies
│   ├── application/           # Application layer
│   │   └── protocols/         # Repository interfaces
│   ├── domain/               # Domain layer
│   │   ├── entities/         # Domain entities
│   │   └── services/         # Business logic
│   └── infra/                # Infrastructure layer
│       ├── auth/             # JWT authentication
│       └── db/               # Database models & repositories
├── alembic/                  # Database migrations
└── tests/                    # Test suites
```

### Frontend (React + TypeScript)
Modern React application with Redux Toolkit for state management:

```
frontend/
├── src/
│   ├── components/           # Reusable UI components
│   ├── pages/               # Page components
│   ├── slices/              # Redux slices
│   ├── hooks/               # Custom React hooks
│   └── utils/               # Utilities (API, etc.)
├── public/                  # Static assets
└── dist/                    # Built application
```

## Prerequisites

- **Docker & Docker Compose** (recommended)
- **Node.js 18+** and **Python 3.10+** (for local development)
- **PostgreSQL** (if running without Docker)

