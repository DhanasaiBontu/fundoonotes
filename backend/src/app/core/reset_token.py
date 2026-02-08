from datetime import datetime, timedelta
from jose import jwt, JWTError

from src.app.core.config import (
    SECRET_KEY,
    ALGORITHM,
    RESET_TOKEN_EXPIRE_MINUTES,
    RESET_TOKEN_PURPOSE
)


def create_reset_token(email: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=RESET_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": email,
        "purpose": RESET_TOKEN_PURPOSE,
        "exp": expire
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_reset_token(token: str) -> str | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if payload.get("purpose") != RESET_TOKEN_PURPOSE:
            return None
        email = payload.get("sub")
        return email
    except JWTError:
        return None
