from .model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, ForeignKey, BigInteger, UniqueConstraint, DateTime, func 
)

class UserEmployee(Base):
    __tablename__ = 'user_employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('user.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())

    # __table_args__ = (UniqueConstraint('user_id', 'employee_id', name='user_employee_user_id_employee_id_key'),)

    # user = relationship("User", back_populates="employee")
    # employee = relationship("Employee", back_populates="user")

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            user_id=data.get('user_id'),
            employee_id=data.get('employee_id')
        )

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'employee_id': self.employee_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }