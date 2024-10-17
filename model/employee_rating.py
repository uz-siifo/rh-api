# # from .model import Base
# from sqlalchemy.orm import relationship
# from sqlalchemy import (
#     Column, Integer, ForeignKey, BigInteger, Boolean, DateTime, func 
# )

# class EmployeeRating(Base):
#     __tablename__ = 'employee_rating'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     is_assiduous = Column(Boolean, nullable=False, default=False)
#     is_collaborative = Column(Boolean, nullable=False, default=False)
#     completed_goals = Column(Integer, nullable=False, default=0)
#     is_punctual = Column(Boolean, nullable=False, default=False)
#     work_quality_rating = Column(Integer, nullable=False, default=0)
#     problem_solving_skills_rating = Column(Integer, nullable=False, default=0)
#     communication_skills_rating = Column(Integer, nullable=False, default=0)
#     time_management_skills_rating = Column(Integer, nullable=False, default=0)
#     leadership_skills_rating = Column(Integer, nullable=False, default=0)
#     employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
#     created_at = Column(DateTime(timezone=True), server_default=func.now())
#     updated_at = Column(DateTime(timezone=True), onupdate=func.now())

#     employee = relationship("Employee", back_populates="rating")

#     @classmethod
#     def to_model(cls, data):
#         return cls(
#             id=data.get('id'),
#             is_assiduous=data.get('is_assiduous', False),
#             is_collaborative=data.get('is_collaborative', False),
#             completed_goals=data.get('completed_goals', 0),
#             is_punctual=data.get('is_punctual', False),
#             work_quality_rating=data.get('work_quality_rating', 0),
#             problem_solving_skills_rating=data.get('problem_solving_skills_rating', 0),
#             communication_skills_rating=data.get('communication_skills_rating', 0),
#             time_management_skills_rating=data.get('time_management_skills_rating', 0),
#             leadership_skills_rating=data.get('leadership_skills_rating', 0),
#             employee_id=data.get('employee_id')
#         )

#     def to_json(self):
#         return {
#             'id': self.id,
#             'is_assiduous': self.is_assiduous,
#             'is_collaborative': self.is_collaborative,
#             'completed_goals': self.completed_goals,
#             'is_punctual': self.is_punctual,
#             'work_quality_rating': self.work_quality_rating,
#             'problem_solving_skills_rating': self.problem_solving_skills_rating,
#             'communication_skills_rating': self.communication_skills_rating,
#             'time_management_skills_rating': self.time_management_skills_rating,
#             'leadership_skills_rating': self.leadership_skills_rating,
#             'employee_id': self.employee_id,
#             'created_at': self.created_at.isoformat() if self.created_at else None,
#             'updated_at': self.updated_at.isoformat() if self.updated_at else None
#         }
