from sqlalchemy.orm import Session

from app.config.db import SessionLocal


def get_session() -> Session:
    with SessionLocal() as session:
        yield session
