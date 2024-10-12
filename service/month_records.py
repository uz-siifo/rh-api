from .service import Service
from sqlalchemy import select, update, delete, or_
from sqlalchemy.orm import Session
from model.models import MonthRecords

class MonthRecordsService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_record = MonthRecords.to_model(data)
                session.add(new_record)
                session.commit()
                return "Month record created successfully"
        except Exception as e:
            return f"Error creating month record: {str(e)}"

    def update(self, data):
        try:
            with Session(self.engine) as session:
                stmt = (
                    update(MonthRecords)
                    .where(MonthRecords.id == data.get('id'))
                    .values(
                        month=data.get('month'),
                        year=data.get('year'),
                        presences=data.get('presences'),
                        absences=data.get('absences')
                    )
                )
                session.execute(stmt)
                session.commit()
                return "Month record updated successfully"
        except Exception as e:
            return f"Error updating month record: {str(e)}"

    def delete(self, data):
        try:
            with Session(self.engine) as session:
                query = delete(MonthRecords).where(
                    or_(
                        MonthRecords.id == data.get('id'),
                        MonthRecords.month == data.get('month'),
                        MonthRecords.year == data.get('year')
                    )
                )
                session.execute(query)
                session.commit()
                return "Month record deleted successfully"
        except Exception as e:
            return f"Error deleting month record: {str(e)}"

    def get_all(self):
        try:
            with Session(self.engine) as session:
                query = select(MonthRecords)
                result = session.execute(query).scalars().all()

                records = [record.to_json() for record in result]
                return records
        except Exception as e:
            return f"Error fetching month records: {str(e)}"
