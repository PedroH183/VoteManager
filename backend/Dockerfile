# Build Runtime 
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Runtime of Api
FROM python:3.10-slim as runtime

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app /app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]

# Build Environment for Postgres
FROM postgres:15 as postgres

ENV POSTGRES_DB=votemanager \
    POSTGRES_USER=votemanager \
    POSTGRES_PASSWORD=changeme \
    POSTGRES_DB_HOST=db \
    POSTGRES_DB_PORT=5432


EXPOSE 5432