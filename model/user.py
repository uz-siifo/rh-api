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

    contacts = relationship("UserContact", back_populates="user", cascade="all, delete", passive_deletes=True) 
    employees = relationship("Employee", secondary="user_employee", back_populates="users") 

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            nickname=data.get('nickname'),
            email=data.get('email'),
            passwd=data.get('passwd'),
            access_level=data.get('access_level')
        )

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'nickname': self.nickname,
            'email': self.email,
            'access_level': self.access_level.name if self.access_level else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'contacts': [contact.to_json() for contact in self.contacts]  # Se a classe UserContact tiver um método to_json()
        }