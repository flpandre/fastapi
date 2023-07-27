from fastapi import APIRouter
from fastapi import Query
from typing import Optional
from sqlalchemy.orm import Session
from fastapi import Request

from app.code.Model.Schema.Entity import EntityCreate
from app.code.Model.Schema.Entity import Entity as EntityModel
from app.code.Model.Repository.Entity import EntityRepository

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/entity",
    tags=["Entity"],
    responses={404: {"description": "Not found"}},
)

@router.get("/{entity_id}", response_model=EntityModel)
def get_entity(entity_id: int):
    return EntityRepository.get_entity(entity_id=entity_id)

@router.post("/")
def create_entity(entity: EntityCreate):
   return EntityRepository.create_entity(entity)

@router.post("/{type}")
async def create_entity(request: Request, type):
   jsonobj = await request.json()
   return type