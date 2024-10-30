from .service import Service
from model.models import Progression
from sqlalchemy.orm import Session

class ProgressionService(Service):
    def __init__(self, engine):
        super().__init__(engine)

    #  {
    #     "id": self.id,
    #     "employee_id": self.employee_id,
    #     "description": self.description,
    #     "created_at": self.created_at,
    #     "updated_at": self.updated_at
    # }

    def create(self, data):
        with Session(self.engine) as session:
            try:
                new_progression = Progression.to_model(data)
                session.add(new_progression)
                session.commit()
                return new_progression.to_json()
                
            except Exception as e:
                session.rollback()
                return e
            
    def update(self, data):
        with Session(self.engine) as session:
            try:
                from sqlalchemy import update

                stmt = None
                for key in data.keys():
                    if (key == "description"):
                        stmt = update(Progression).where(
                            Progression.id == data.get("id")
                        ).values(
                            description = data.get("description")
                        )     

                    if (key == "employee_id"):
                        stmt = update(Progression).where(
                            Progression.id == data.get("id")
                        ).values(
                            employee_id = data.get("employee_id")
                        )
                session.execute(stmt)
                session.commit()
                return {"status": "OK"}

            except Exception as e:
                session.rollback()
                return e
    
    def delete(self, data):
        with Session(self.engine) as session:
            try:
                from sqlalchemy import delete
                stmt = delete(Progression).where(id == data.get("id"))
                session.execute(stmt)
                session.commit()
                return {"status": "OK"}
            except Exception as e:
                session.rollback()
                return e

    def get_all(self):
        with Session(self.engine) as session:
            from sqlalchemy import select
            query = select(Progression)
            result = session.execute(query).scalars().all()
            progressions = [progression.to_json() for progression in result]
            return progressions

    def get_by_employee_id(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import select
            query = select(Progression).where(
                Progression.employee_id == data.get("employee_id")
            )
            result = session.execute(query).scalars().all()
            progressions = [progression.to_json() for progression in result]
            return progressions
            
        
    