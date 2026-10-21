import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy.orm.mapper import configure_mappers

from iris_mnemosia_backend.core.config.business_exception_handler import (
    business_exception_handler,
)
from iris_mnemosia_backend.core.config.config import Settings
from iris_mnemosia_backend.core.config.database import Database
from iris_mnemosia_backend.core.config.logger_config import logger_config
from iris_mnemosia_backend.core.exceptions.business_exception import BusinessException
from iris_mnemosia_backend.routes import categories, resources, status

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Settings are already validated by Settings()
    settings = Settings()
    logger_config(settings.debug)
    logger.info("Starting API")

    app.state.database = Database(database_path=settings.database_path)
    logger.debug("Database stored in app state")
    logger.debug("Configuring database mappers")
    configure_mappers()
    yield
    logger.info("Shutdown in progress")
    app.state.database.dispose()
    logger.debug("Closed connection pool")


app = FastAPI(lifespan=lifespan)
app.include_router(status.router)
app.include_router(categories.router)
app.include_router(resources.router)

app.add_exception_handler(BusinessException, business_exception_handler)
