from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.app.db.session import get_db
from src.app.schemas.label import LabelCreate, LabelResponse
from src.app.services.label_service import create_label, get_labels
from src.app.core.dependencies import get_current_user

router = APIRouter(prefix="/labels", tags=["Labels"])


@router.post("/", response_model=LabelResponse)
def create(
    label_in: LabelCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return create_label(db, label_in.name, current_user.id)


@router.get("/", response_model=list[LabelResponse])
def list_labels(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    return get_labels(db, current_user.id)
