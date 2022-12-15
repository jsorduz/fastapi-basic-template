import pytest
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.pool import StaticPool
from starlette.testclient import TestClient

from app.api.v1.deps import get_session
from app.config.db import Base
from app.main import app

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
SessionLocalTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_test_db() -> Session:
    with SessionLocalTesting() as session:
        yield session


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    app.dependency_overrides[get_session] = get_test_db
    yield


@pytest.fixture(scope="function", autouse=True)
def clean_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture()
def client():
    with TestClient(app) as cli:
        yield cli
