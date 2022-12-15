from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.deps import get_session
from app.helpers import get_password_hash
from app.models import User
from app.schemas.v1.schemas import UserCreateSchema, UserSchema

router = APIRouter()


@router.get("/", response_model=list[UserSchema])
def list_users(
    session: Session = Depends(get_session),
    skip: int = 0,
    limit: int = 100,
):
    return session.query(User).offset(skip).limit(limit).all()


@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user(user_create: UserCreateSchema, session: Session = Depends(get_session)):
    existing_user = session.query(User).filter(User.email == user_create.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = User(
        email=user_create.email,
        hashed_password=(get_password_hash(user_create.password)),
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
