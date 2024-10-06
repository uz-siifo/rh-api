from .model import Base
from sqlalchemy.orm import relationship
from utils.enums import FeedbackEnum
from sqlalchemy import (
    Column, Integer, ForeignKey, BigInteger, Enum, DateTime, func 
)

class PerformanceEvaluation(Base):
    __tablename__ = 'performance_evaluation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    employee_rating_id = Column(BigInteger, ForeignKey('employee_rating.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    employee_goals_id = Column(BigInteger, ForeignKey('goals.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    feedback = Column(Enum(FeedbackEnum), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    employee = relationship("Employee")
    employee_rating = relationship("EmployeeRating")
    employee_goals = relationship("Goals")