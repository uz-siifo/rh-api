from .model import Base
from sqlalchemy.types import Enum as PgEnum
from utils.enums import AccessLevelEnum
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, String, DateTime, func 
)

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    nickname = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    passwd = Column(String(255), nullable=False)
    access_level = Column(PgEnum(AccessLevelEnum, name="access_level_enum"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    contacts = relationship("UserContact", back_populates="user")  