from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.app.schemas.user import UserCreate, UserResponse
from src.app.services.user_service import get_user_by_email, create_user
from src.app.db.session import get_db
from src.app.core.logger import logger


router = APIRouter(prefix="/users", tags=["Users"])


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    logger.info(f"Register attempt for email: {user_in.email}")

    existing_user = get_user_by_email(db, user_in.email)
    if existing_user:
        logger.warning(f"Registration failed, email already exists: {user_in.email}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    user = create_user(db, user_in)
    logger.info(f"User registered successfully: {user.email}")
    return user

from src.app.core.dependencies import get_current_user
from src.app.models.user import User


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user
