from sqlalchemy.orm import Session

from src.app.models.user import User
from src.app.schemas.user import UserCreate
from src.app.core.security import hash_password



def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user_in: UserCreate) -> User:
    hashed_pwd = hash_password(user_in.password)

    user = User(
        email=user_in.email,
        hashed_password=hashed_pwd
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user_password(db: Session, user: User, new_password: str) -> User:
    user.hashed_password = hash_password(new_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

