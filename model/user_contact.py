from .model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, String, DateTime, BigInteger, ForeignKey, func 
)

class UserContact(Base):
    __tablename__ = 'user_contact'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('user.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    contact = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="contacts")

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            user_id=data.get('user_id'),
            contact=data.get('contact')
        )

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'contact': self.contact,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }