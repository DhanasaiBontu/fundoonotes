from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from src.app.schemas.note import NoteCreate, NoteUpdate, NoteResponse
from src.app.services.note_service import (
    create_note,
    get_notes,
    get_note_by_id,
    update_note,
    delete_note
)
from src.app.core.dependencies import get_current_user
from src.app.db.session import get_db
from src.app.models.user import User

router = APIRouter(prefix="/notes", tags=["Notes"])


@router.post("/", response_model=NoteResponse)
def create(payload: NoteCreate,
           db: Session = Depends(get_db),
           user: User = Depends(get_current_user)):
    return create_note(db, user, payload)


@router.get("/", response_model=List[NoteResponse])
def list_notes(db: Session = Depends(get_db),
               user: User = Depends(get_current_user)):
    return get_notes(db, user)


@router.get("/{note_id}", response_model=NoteResponse)
def get(note_id: int,
        db: Session = Depends(get_db),
        user: User = Depends(get_current_user)):
    note = get_note_by_id(db, user, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note


@router.put("/{note_id}", response_model=NoteResponse)
def update(note_id: int,
           payload: NoteUpdate,
           db: Session = Depends(get_db),
           user: User = Depends(get_current_user)):
    note = get_note_by_id(db, user, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return update_note(db, note, payload)


@router.delete("/{note_id}")
def delete(note_id: int,
           db: Session = Depends(get_db),
           user: User = Depends(get_current_user)):
    note = get_note_by_id(db, user, note_id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    delete_note(db, note)
    return {"message": "Note deleted"}
