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
    
    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            employee_id=data.get('employee_id'),
            employee_rating_id=data.get('employee_rating_id'),
            employee_goals_id=data.get('employee_goals_id'),
            feedback=data.get('feedback')
        )

    def to_json(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'employee_rating_id': self.employee_rating_id,
            'employee_goals_id': self.employee_goals_id,
            'feedback': self.feedback.value if self.feedback else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }