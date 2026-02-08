from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.app.schemas.auth import LoginRequest, TokenResponse
from src.app.services.user_service import get_user_by_email
from src.app.core.security import verify_password
from src.app.core.jwt import create_access_token
from src.app.db.session import get_db
from src.app.core.logger import logger

from src.app.schemas.password_reset import ForgotPasswordRequest, ResetPasswordRequest
from src.app.core.reset_token import create_reset_token, verify_reset_token
from src.app.services.user_service import update_user_password


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=TokenResponse)
def login(user_in: LoginRequest, db: Session = Depends(get_db)):
    logger.info(f"Login attempt for email: {user_in.email}")

    user = get_user_by_email(db, user_in.email)
    if not user:
        logger.warning("Login failed: user not found")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    if not verify_password(user_in.password, user.hashed_password):
        logger.warning("Login failed: invalid password")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    access_token = create_access_token({"sub": user.email})
    logger.info(f"Login successful for email: {user.email}")

    return TokenResponse(access_token=access_token)

@router.post("/forgot-password")
def forgot_password(payload: ForgotPasswordRequest, db: Session = Depends(get_db)):
    user = get_user_by_email(db, payload.email)

    # Security best practice: don't reveal if email exists
    if not user:
        logger.info(f"Forgot password requested for non-existing email: {payload.email}")
        return {"message": "If the email exists, a reset link has been generated."}

    token = create_reset_token(user.email)

    # In real app: send email. For now: log it.
    logger.info(f"Password reset token for {user.email}: {token}")

    return {"message": "If the email exists, a reset link has been generated."}


@router.post("/reset-password")
def reset_password(payload: ResetPasswordRequest, db: Session = Depends(get_db)):
    email = verify_reset_token(payload.token)
    if not email:
        raise HTTPException(status_code=400, detail="Invalid or expired token")

    user = get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid token")

    update_user_password(db, user, payload.new_password)
    logger.info(f"Password reset successful for {email}")

    return {"message": "Password has been reset successfully"}
