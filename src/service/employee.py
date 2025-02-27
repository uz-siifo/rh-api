from .service import Service
from sqlalchemy import select, update, delete, or_, insert
from sqlalchemy.orm import Session
from model.models import Employee

class EmployeeService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        # esta func cria um usuario e um empregado ja associados

        user = {
            "name": data.get('name'),
            "nickname": data.get('nickname'),
            "username": data.get('username'),
            "email": data.get('email'),
            "passwd": data.get('passwd'),
            "role": data.get('role'),
            "contact": data.get("contact")
        }

        employee = {
            "position_at_work": data.get('position'),
            "state": data.get("state"),
            "length_of_service": data.get("length_of_service"),
            "date_admission": data.get('date_admission'),
            'academic_level': data.get('academic_level'),
            "department_id": 0
        }
            
        with Session(self.engine) as session:
            try:
                from model.models import User
                from service.user_employee import UserEmployeeService
                from service.department import DepartmentService

                user_employee_service = UserEmployeeService(self.engine)
                department_service = DepartmentService(self.engine)
                department = department_service.get_by_name({"department_name": data.get("department")})
                employee.update({"department_id": department.get("id")})
                
                new_employee = Employee.to_model(employee)
                new_user = User.to_model(user)
                
                session.add(new_employee)
                session.add(new_user)
                session.commit()
                employee_id = new_employee.to_json().get("id")
                user_id = new_user.to_json().get("id")
                
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
                employee = session.query(Employee).filter(Employee.id == data.get("id")).first()

                for key, value in data.items():
                    if (hasattr(employee, key)):
                        setattr(employee, key, value)

                session.commit()
                return employee.to_json()
            except Exception as e:
                session.rollback()
                return e

    def delete(self, data):
        with Session(self.engine) as session:    
            try:
                query = delete(Employee).where(
                    Employee.id == data.get('id')
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