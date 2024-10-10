from .service import Service
from sqlalchemy import select
from sqlalchemy.orm import Session
from model.employee import Employee

class EmployeeService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        
        with Session(self.engine) as session:

            session.add(Employee.to_model(data))
            session.commit()
            return {"OK"}

    def update(self, data):
        from sqlalchemy import update
        with Session(self.engine) as session:
            new_employee = Employee.to_model(data)
            session.query(Employee).filter(Employee.id == data.get('id')).update(
                new_employee.to_json()
            )

            session.commit()
            return "OK"

    def delete(self, data):
        pass

    def get_all(self):
        with Session(self.engine) as session:
            from sqlalchemy import Select
            query = Select(Employee)
            result = session.execute(query).fetchall()

            employees = []

            for row in result:
                employee = row.tuple()[0]
                employees.append(employee.to_json())

            return employees