from fastapi import APIRouter
from src.app.api.v1.routers.user import router as user_router
from src.app.api.v1.routers.auth import router as auth_router

from src.app.api.v1.routers.note import router as note_router

from src.app.api.v1.routers import labels

api_router = APIRouter()
api_router.include_router(user_router)
api_router.include_router(auth_router)

api_router.include_router(note_router)

api_router.include_router(labels.router)

