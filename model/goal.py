from .model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, Text, DateTime, BigInteger, ForeignKey, func 
)

class Goals(Base):
    __tablename__ = 'goals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text, nullable=False)
    start_date = Column(DateTime, nullable=False)
    conclusion_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    employee = relationship("Employee")