from .service import Service
from sqlalchemy import select, update, delete, or_
from sqlalchemy.orm import Session
from model.models import Employee

class EmployeeService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_employee = Employee.to_model(data)
                session.add(new_employee)
                session.commit()
                return "Employee created successfully"
        except Exception as e:
            return f"Error creating employee: {str(e)}"

    def update(self, data):
        try:
            with Session(self.engine) as session:
                stmt = (
                    update(Employee)
                    .where(Employee.id == data.get('id'))
                    .values(
                        name=data.get('name'),
                        identity_card_bi=data.get('identity_card_bi'),
                        position=data.get('position'),
                        department=data.get('department')
                    )
                )
                session.execute(stmt)
                session.commit()
                return "Employee updated successfully"
        except Exception as e:
            return f"Error updating employee: {str(e)}"

    def delete(self, data):
        try:
            with Session(self.engine) as session:
                query = delete(Employee).where(
                    or_(
                        Employee.id == data.get('id'),
                        Employee.identity_card_bi.like(data.get('identity_card_bi'))
                    )
                )
                session.execute(query)
                session.commit()
                return "Employee deleted successfully"
        except Exception as e:
            return f"Error deleting employee: {str(e)}"

    def get_all(self):
        try:
            with Session(self.engine) as session:
                query = select(Employee)
                result = session.execute(query).scalars().all()

                employees = [employee.to_json() for employee in result]
                return employees
        except Exception as e:
            return f"Error fetching employees: {str(e)}"
