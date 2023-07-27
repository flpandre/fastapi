from pydantic import BaseModel

class EntityBase(BaseModel):
    type: str

class EntityCreate(EntityBase):
    pass

class Entity(EntityBase):
    entity_id: int
    type: str

    class Config:
        orm_mode = True