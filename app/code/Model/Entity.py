from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.code.Database.database import Base
metadata = Base.metadata

class Entity(Base):
    __tablename__ = "entity"

    entity_id = Column(Integer, primary_key=True, index=True)
    type = Column(String, unique=True, index=True)