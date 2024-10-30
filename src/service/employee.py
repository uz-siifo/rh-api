from .service import Service
from sqlalchemy import select, update, delete, or_, insert
from sqlalchemy.orm import Session
from model.models import Employee

class EmployeeService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, employee, user):
        # esta func cria um usuario e um empregado ja associados
        with Session(self.engine) as session:
            try:
                from model.models import User
                from model.models import UserEmployee
                from service.user_employee import UserEmployeeService
                new_employee = Employee.to_model(employee)
                new_user = User.to_model(user)
                session.add(new_employee)
                session.add(new_user)
                session.commit()
                employee_id = new_employee.to_json().get("id")
                user_id = new_user.to_json().get("id")
                user_employee_service = UserEmployeeService(self.engine)
                relation = user_employee_service.create({
                    "user_id": user_id,
                    "employee_id": employee_id
                })
                return {
                        "employee": new_employee.to_json(),
                        "user": new_user.to_json(),
                        "user_employee": relation
                    }
            except Exception as e:
                session.rollback()
                return e

    def update(self, data):
        with Session(self.engine) as session:            
            try:    
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
                return {"status": "OK"}
            except Exception as e:
                session.rollback()
                return e

    def delete(self, data):
        with Session(self.engine) as session:    
            try:
                query = delete(Employee).where(
                    or_(
                        Employee.id == data.get('id'),
                        Employee.identity_card_bi.like(data.get('identity_card_bi'))
                    )
                )
                session.execute(query)
                session.commit()
                return {"status": "OK"}
            except Exception as e:
                session.rollback()
                return e

    def get_all(self):
        try:
            with Session(self.engine) as session:
                from model.models import User, UserEmployee
                from sqlalchemy import and_
                query = select(
                    User.name, User.nickname, User.email, 
                    Employee
                ).where(
                    and_(
                        UserEmployee.employee_id == Employee.id,
                        UserEmployee.user_id == User.id
                    )
                )
                result = session.execute(query).fetchall()
                employees =[]
                for row in result:
                    employee = row.tuple()
                    employees.append({
                        "name": employee[0],
                        "nickname": employee[1],
                        "email": employee[2],
                        "employee": employee[3].to_json()
                    })

                return employees
        except Exception as e:
            return f"Error fetching employees: {str(e)}"
        
    def get_all_by_department(self, data):
        try:
            with Session(self.engine) as session:
                from sqlalchemy import select
                from model.models import User

                query = select(
                    User.name, User.nickname, User.email, 
                    Employee
                ).where(
                    Employee.department_id == data.get("department_id")
                )
                result = session.execute(query).fetchall()
                employees = []
                for row in result:
                    employee = row.tuple()
                    employees.append({
                        "name": employee[0],
                        "nickname": employee[1],
                        "email": employee[2],
                        "employee": employee[3].to_json()
                    })

                return employees
        except Exception as e:
            return e