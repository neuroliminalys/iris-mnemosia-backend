from typing import Annotated

from fastapi import APIRouter, Depends
from iris_mnemosia_backend.infrastructure.database import open_new_session
from sqlalchemy import text
from sqlalchemy.orm import Session

router = APIRouter(prefix="/status", tags=["status"])

@router.get("/api")
def get_status():
    return {"status": "ok"}

@router.get("/database")
def get_database_status(session: Annotated[Session, Depends(open_new_session)]):
    session.execute(text("SELECT 1"))
    return {"status": "ok"}