from .model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, ForeignKey, BigInteger, DateTime, func 
)

class Presences(Base):
    __tablename__ = 'presences'

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    month_records_id = Column(BigInteger, ForeignKey('month_records.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    employee = relationship("Employee")
    month_record = relationship("MonthRecords")
