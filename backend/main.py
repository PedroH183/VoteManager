from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.infra.db.database import Base, engine
from app.api.routers.session_router import router as session_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: criar tabelas e abrir conexões
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown: fechar engine
    await engine.dispose()

app = FastAPI(
    lifespan=lifespan,
    version="1.0.0",
    title="Voting Session API",
)
origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(session_router)
# uvicorn main:app --reload --host 0.0.0.0 --port 8000


@app.get("/api/health")
def root():
    return {"message": "Working ..."}
