from sqlalchemy.orm import Session
from typing import List

from src.app.models.note import Note
from src.app.schemas.note import NoteCreate, NoteUpdate
from src.app.models.user import User


def create_note(db: Session, user: User, payload: NoteCreate) -> Note:
    note = Note(
        title=payload.title,
        description=payload.description,
        owner_id=user.id
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def get_notes(db: Session, user: User) -> List[Note]:
    return db.query(Note).filter(
        Note.owner_id == user.id,
        Note.is_deleted == False
    ).all()


def get_note_by_id(db: Session, user: User, note_id: int) -> Note | None:
    return db.query(Note).filter(
        Note.id == note_id,
        Note.owner_id == user.id
    ).first()


def update_note(db: Session, note: Note, payload: NoteUpdate) -> Note:
    for field, value in payload.dict(exclude_unset=True).items():
        setattr(note, field, value)

    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def delete_note(db: Session, note: Note):
    note.is_deleted = True
    db.add(note)
    db.commit()
