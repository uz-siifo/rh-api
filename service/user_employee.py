from .service import Service
from sqlalchemy.orm import Session
from model.user_employee import UserEmployee

class UserEmployeeService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        with Session(self.engine) as session:
            session.add(UserEmployee.to_model(data))
            session.commit()
            return "OK"
        
    def delete(self, data):
        from sqlalchemy import delete
        with Session(self.engine) as session:
            query = delete(UserEmployee).where(UserEmployee.id == data.get('id'))
            session.execute(query)
            session.commit()
            return "OK"

    def update(self, data):
        with Session(self.engine) as session:
            pass

    def get_all(self):
        from sqlalchemy import Select
        with Session(self.engine) as session:
            query = Select(UserEmployee)
            result = session.execute(query).fetchall()
            user_employees = []

            for row in result:
                user_employee = row.tuple()[0]
                user_employees.append(user_employee.to_json())
            
            return user_employees