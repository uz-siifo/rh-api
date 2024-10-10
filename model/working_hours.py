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

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            normal_hours=data.get('normal_hours', 0),
            overtime=data.get('overtime', 0),
            employee_id=data.get('employee_id')
        )

    def to_json(self):
        return {
            'id': self.id,
            'normal_hours': self.normal_hours,
            'overtime': self.overtime,
            'employee_id': self.employee_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
