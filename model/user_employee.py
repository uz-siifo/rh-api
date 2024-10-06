from .model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, ForeignKey, BigInteger, UniqueConstraint, DateTime, func 
)

class UserEmployee(Base):
    __tablename__ = 'user_employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('user.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())

    __table_args__ = (UniqueConstraint('user_id', 'employee_id', name='user_employee_user_id_employee_id_key'),)

    user = relationship("User")
    employee = relationship("Employee")