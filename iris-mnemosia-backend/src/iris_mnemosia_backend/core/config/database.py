import logging
from collections.abc import Iterator

from fastapi import Request
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.schema import MetaData

logger = logging.getLogger(__name__)

naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class DatabaseModel(DeclarativeBase):
    metadata = MetaData(naming_convention=naming_convention)


class Database:
    engine: Engine
    New_session: sessionmaker[Session]

    def __init__(self, database_path: str):
        logger.debug("Creating database engine...")
        self.engine = create_engine(database_path)
        logger.debug("Successfully created database engine")
        logger.debug("Creating session factory...")
        self.New_session = sessionmaker(bind=self.engine)
        logger.debug("Successfully created session factory")

    def open_new_session(self) -> Session:
        return self.New_session()

    def dispose(self) -> None:
        self.engine.dispose()


def open_new_session(request: Request) -> Iterator[Session]:
    database: Database = request.app.state.database
    with database.open_new_session() as session:
        try:
            logger.debug(f"Opening new session with id {id(session)}")
            yield session
            session.commit()
            logger.debug("Committed changes to database")
        except Exception:
            session.rollback()
            logger.error("Exception happended, rolled back database")
            raise
        finally:
            logger.debug(f"Closed session with id {id(session)}")
