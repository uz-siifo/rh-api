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
            return e

    def update(self, data):
        try:
            with Session(self.engine) as session:
                working_hours = session.query(WorkingHours).filter(WorkingHours.id == data.get("id")).first()
                for key, value in data.items():
                    if (hasattr(working_hours, key)):
                        setattr(working_hours, key, value)
                session.commit()
                return working_hours.to_json()
        except Exception as e:
            return e

    def delete(self, data):
        try:
            with Session(self.engine) as session:
                query = delete(WorkingHours).where(
                    WorkingHours.id == data.get('id')
                )
                session.execute(query)
                session.commit()
                return {"status": "OK"}
        except Exception as e:
            return e

    def get_all(self):
        with Session(self.engine) as session:
            try:
                query = select(WorkingHours)
                result = session.execute(query).scalars().all()
                working_hours = [working_hour.to_json() for working_hour in result]
                return working_hours
            except Exception as e:
                return e
            
    def get_by_employee(self, data):
        with Session(self.engine) as session:
            try:
                from sqlalchemy import select
                query = select(WorkingHours).where(
                    WorkingHours.employee_id == data.get("employee_id")
                )
                result = session.execute(query).scalars().all()
                working_hours = [working_hour.to_json() for working_hour in result]
                return working_hours
            except Exception as e:
                return e