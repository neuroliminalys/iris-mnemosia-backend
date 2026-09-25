
from contextlib import asynccontextmanager

from fastapi import FastAPI

from iris_mnemosia_backend.core.config.config import Settings
from iris_mnemosia_backend.infrastructure.database import Database
from iris_mnemosia_backend.routes import status


@asynccontextmanager
async def lifespan(app: FastAPI):
    # TODO: log startup
    settings = Settings()
    # TODO : log model validation
    Settings.model_validate(settings)
    app.state.database = Database(database_path=settings.database_path, logger="")
    yield
    # Closes the current connection pool
    app.state.database.dispose()
    # TODO: log shutdown

app = FastAPI(lifespan=lifespan)
app.include_router(status.router)
