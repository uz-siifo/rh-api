from .service import Service
from sqlalchemy import select, update, delete, or_
from sqlalchemy.orm import Session
from model.models import Presences

class PresencesService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        with Session(self.engine) as session:    
            try:    
                new_presence = Presences.to_model(data)
                session.add(new_presence)
                session.commit()
                return new_presence.to_json()
            except Exception as e:
                session.rollback()
                return e

    def update(self, data):
        try:
            with Session(self.engine) as session:
                presence = session.query(Presences).filter(Presences.id == data.get("id")).first()
                for key, value in data.items():
                    if (hasattr(presence, key)):
                        setattr(presence, key, value)
                session.commit()
                return presence.to_json()
        except Exception as e:
            return e

    def delete(self, data):
            with Session(self.engine) as session:
                try:
                    query = delete(Presences).where(
                        Presences.id == data.get('id')
                    )
                    session.execute(query)
                    session.commit()
                    return {"status": "OK"}
                except Exception as e:
                    session.rollback()
                    return e

    def get_all(self):
        with Session(self.engine) as session:
            query = select(Presences)
            result = session.execute(query).scalars().all()

            presences = [presence.to_json() for presence in result]
            return presences


    def get_by_employee(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import select
            query = select(Presences).where(
                Presences.employee_id == data.get("employee_id")
            )
            result = session.execute(query).scalars().all()
            presences = [presence.to_json() for presence in result]
            return presences