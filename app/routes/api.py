from fastapi import APIRouter
from app.code.Endpoints import Entity

router = APIRouter()
router.include_router(Entity.router)