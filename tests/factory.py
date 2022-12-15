from app.helpers import get_password_hash
from app.models import User
from tests.conftest import SessionLocalTesting


def create_user(email: str, password: str = "s3cret", **kwargs):
    with SessionLocalTesting() as session:
        user = User(email=email, hashed_password=get_password_hash(password), **kwargs)
        session.add(user)
        session.commit()
