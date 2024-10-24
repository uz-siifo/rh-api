from .service import Service
from model.models import Progression
from sqlalchemy.orm import Session

class ProgressionService(Service):
    def __init__(self, engine):
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_progression = Progression.to_model(data)
                session.add(new_progression)
                session.commit()
                return new_progression.to_json()
            return "Bad"
            
        except Exception as error:
            return str(error)
        
    def update(self, data):
        pass

    
    def delete(self, data):
        pass

    def get_all(self):
        pass

    def get_by_employee(self, data):
        pass
    