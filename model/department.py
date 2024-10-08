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