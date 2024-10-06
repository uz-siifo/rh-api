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