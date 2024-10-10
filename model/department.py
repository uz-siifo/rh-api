from .model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, BigInteger, Float, String, DateTime, func 
)

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    employee_nums = Column(BigInteger, nullable=False, default=0)
    min_salary = Column(Float, nullable=False, default=0)
    max_salary = Column(Float, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    employees = relationship("Employee", back_populates="department")

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            employee_nums=data.get('employee_nums', 0),
            min_salary=data.get('min_salary', 0.0),
            max_salary=data.get('max_salary', 0.0)
        )

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'employee_nums': self.employee_nums,
            'min_salary': self.min_salary,
            'max_salary': self.max_salary,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }