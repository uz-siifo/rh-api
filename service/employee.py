from .service import Service
from sqlalchemy import select
from sqlalchemy.orm import Session
from model.employee import Employee

class EmployeeService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        
        with Session(self.engine) as session:
            employee = Employee(
                nuit = data.get('nuit'),
                identity_card_bi = data.get('identity_card_bi'),
                salary = data.get('salary'),
                data_admission = data.get('data_admission'),
                department_id = data.get('department_id'),
                academic_level = data.get('academic_level')
            )

            session.add(employee)
            session.commit()


            return {"OK"}

    def update(self, data):
        pass

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
                employees.append({
                    "name": "employee_name",
                    "nickname": "employee_nickname",
                    "nuit": employee.nuit,
                    "identity_card_bi": employee.identity_card_bi,
                    "position_at_work": employee.position_at_work,
                    "date_admission": employee.date_admission,
                    "department_id": employee.department_id,
                    "academic_level": employee.academic_level, 
                    "salary": employee.salary,
                    "created_at": employee.created_at,
                    "updated_at": employee.updated_at
                })