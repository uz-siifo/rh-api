from .model import Base
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column, Integer, String, UniqueConstraint, DateTime, func 
)

class MonthRecords(Base):
    __tablename__ = 'month_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    month = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    presences = Column(Integer, nullable=False, default=0)
    absences = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    __table_args__ = (UniqueConstraint('month', 'year', name='month_records_month_year_key'),)


    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            month=data.get('month'),
            year=data.get('year'),
            presences=data.get('presences', 0),
            absences=data.get('absences', 0)
        )

    def to_json(self):
        return {
            'id': self.id,
            'month': self.month,
            'year': self.year,
            'presences': self.presences,
            'absences': self.absences,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
