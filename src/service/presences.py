from .service import Service
from sqlalchemy import select, update, delete, or_
from sqlalchemy.orm import Session
from model.models import Presences

class PresencesService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_presence = Presences.to_model(data)
                session.add(new_presence)
                session.commit()
                return new_presence.to_json()
        except Exception as e:
            return f"Error creating presence record: {str(e)}"

    def update(self, data):
        try:
            with Session(self.engine) as session:
                stmt = (
                    update(Presences)
                    .where(Presences.id == data.get('id'))
                    .values(
                        employee_id=data.get('employee_id'),
                        month_records_id=data.get('month_records_id')
                    )
                )
                session.execute(stmt)
                session.commit()
                return "Presence record updated successfully"
        except Exception as e:
            return f"Error updating presence record: {str(e)}"

    def delete(self, data):
        try:
            with Session(self.engine) as session:
                query = delete(Presences).where(
                    Presences.id == data.get('id')
                )
                session.execute(query)
                session.commit()
                return "Presence record deleted successfully"
        except Exception as e:
            return f"Error deleting presence record: {str(e)}"

    def get_all(self):
        try:
            with Session(self.engine) as session:
                query = select(Presences)
                result = session.execute(query).scalars().all()

                presences = [presence.to_json() for presence in result]
                return presences
        except Exception as e:
            return f"Error fetching presence records: {str(e)}"
