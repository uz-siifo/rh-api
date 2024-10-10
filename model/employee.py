from .model import Base
from utils.enums import PositionAtWorkEnum
from sqlalchemy.orm import relationship
from model.department import Department
from model.employee_rating import EmployeeRating

from sqlalchemy import (
    Column, Integer, BigInteger, Float, String,ForeignKey, Enum, DateTime, func 
)

class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    position_at_work = Column(Enum(PositionAtWorkEnum, name="position_at_work_enum", create_type=False), nullable=False)
    nuit = Column(BigInteger, nullable=False)
    identity_card_bi = Column(String(255), nullable=False)
    salary = Column(Float, nullable=False, default=0)
    date_admission = Column(DateTime, nullable=False)
    academic_level = Column(String(255), nullable=False)
    department_id = Column(BigInteger, ForeignKey('department.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    department = relationship("Department", back_populates="employees")
    rating = relationship("EmployeeRating", back_populates="employee")
    users = relationship("User", secondary="user_employee", back_populates="employees")

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            position_at_work=data.get('position_at_work'),
            nuit=data.get('nuit'),
            identity_card_bi=data.get('identity_card_bi'),
            salary=data.get('salary', 0),
            date_admission=data.get('date_admission'),
            academic_level=data.get('academic_level'),
            department_id=data.get('department_id')
        )

    def to_json(self):
        return {
            'id': self.id,
            'position_at_work': self.position_at_work.name if self.position_at_work else None,
            'nuit': self.nuit,
            'identity_card_bi': self.identity_card_bi,
            'salary': self.salary,
            'date_admission': self.date_admission.isoformat() if self.date_admission else None,
            'academic_level': self.academic_level,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'department_id': self.department_id
        }