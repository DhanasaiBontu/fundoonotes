from sqlalchemy.orm import Session
from src.app.models.label import Label


def create_label(db: Session, name: str, user_id: int):
    label = Label(name=name, user_id=user_id)
    db.add(label)
    db.commit()
    db.refresh(label)
    return label


def get_labels(db: Session, user_id: int):
    return db.query(Label).filter(Label.user_id == user_id).all()
