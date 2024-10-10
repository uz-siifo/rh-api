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

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            employee_id=data.get('employee_id'),
            month_records_id=data.get('month_records_id')
        )

    def to_json(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'month_records_id': self.month_records_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
