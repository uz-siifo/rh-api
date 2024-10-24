from .service import Service
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from model.models import WorkingHours

class WorkingHoursService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_working_hours = WorkingHours.to_model(data)
                session.add(new_working_hours)
                session.commit()
                return new_working_hours.to_json()
        except Exception as e:
            return f"Error creating working hours record: {str(e)}"

    def update(self, data):
        try:
            with Session(self.engine) as session:
                stmt = (
                    update(WorkingHours)
                    .where(WorkingHours.id == data.get('id'))
                    .values(
                        normal_hours=data.get('normal_hours', 0),
                        overtime=data.get('overtime', 0),
                        employee_id=data.get('employee_id')
                    )
                )
                session.execute(stmt)
                session.commit()
                return "Working hours record updated successfully"
        except Exception as e:
            return f"Error updating working hours record: {str(e)}"

    def delete(self, data):
        try:
            with Session(self.engine) as session:
                query = delete(WorkingHours).where(
                    WorkingHours.id == data.get('id')
                )
                session.execute(query)
                session.commit()
                return "Working hours record deleted successfully"
        except Exception as e:
            return f"Error deleting working hours record: {str(e)}"

    def get_all(self):
        try:
            with Session(self.engine) as session:
                query = select(WorkingHours)
                result = session.execute(query).scalars().all()

                working_hours = [wh.to_json() for wh in result]
                return working_hours
        except Exception as e:
            return f"Error fetching working hours records: {str(e)}"
