from .model import Base
from utils.enums import PositionAtWorkEnum
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
    department_id = Column(BigInteger, ForeignKey('department.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    academic_level = Column(String(255), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())