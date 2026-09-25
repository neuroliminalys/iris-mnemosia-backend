from collections.abc import Generator
from logging import Logger

from fastapi import Request
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker


class DatabaseModel(DeclarativeBase):
    pass


class Database:
    logger: Logger
    engine: Engine
    New_session: sessionmaker[Session]

    def __init__(self, database_path: str, logger: Logger):
        self.logger = logger
        self.engine = create_engine(database_path)
        self.New_session = sessionmaker(bind=self.engine)

    def open_new_session(self) -> Session:
        return self.New_session()

    def dispose(self) -> None:
        self.engine.dispose()

def open_new_session(request: Request) -> Generator[Session, None, None]:
    database: Database = request.app.state.database
    with database.open_new_session() as session:
        yield session