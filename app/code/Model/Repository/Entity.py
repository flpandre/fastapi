from app.code.Model.Schema import Entity as EntitySchema
from app.code.Model.Entity import Entity
from app.code.Database.database import SessionLocal

class EntityRepository:
    def create_entity(entity: EntitySchema.EntityCreate):
        entity = Entity(type=entity.type)
        db = SessionLocal()
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def get_entity(entity_id: int):
        db = SessionLocal()
        return db.query(Entity).filter(Entity.entity_id == entity_id).first()