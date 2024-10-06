from .model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, DateTime, BigInteger, ForeignKey, func 
)

class WorkingHours(Base):
    __tablename__ = 'working_hours'

    id = Column(Integer, primary_key=True, autoincrement=True)
    normal_hours = Column(Integer, nullable=False, default=0)
    overtime = Column(Integer, nullable=False, default=0)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    employee = relationship("Employee")
