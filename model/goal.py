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
   
    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            description=data.get('description'),
            start_date=data.get('start_date'),
            conclusion_date=data.get('conclusion_date'),
            end_date=data.get('end_date'),
            employee_id=data.get('employee_id')
        )

    def to_json(self):

        return {
            'id': self.id,
            'description': self.description,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'conclusion_date': self.conclusion_date.isoformat() if self.conclusion_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'employee_id': self.employee_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }