from .model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, ForeignKey, BigInteger, Boolean, DateTime, func 
)

class EmployeeRating(Base):
    __tablename__ = 'employee_rating'

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_assiduous = Column(Boolean, nullable=False, default=False)
    is_collaborative = Column(Boolean, nullable=False, default=False)
    completed_goals = Column(Integer, nullable=False, default=0)
    is_punctual = Column(Boolean, nullable=False, default=False)
    work_quality_rating = Column(Integer, nullable=False, default=0)
    problem_solving_skills_rating = Column(Integer, nullable=False, default=0)
    communication_skills_rating = Column(Integer, nullable=False, default=0)
    time_management_skills_rating = Column(Integer, nullable=False, default=0)
    leadership_skills_rating = Column(Integer, nullable=False, default=0)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    employee = relationship("Employee", back_populates="rating")
