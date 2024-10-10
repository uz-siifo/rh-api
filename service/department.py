from service.service import Service
from sqlalchemy.orm import Session
from model.department import Department

class DepartmentService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)
    
    def create(self, data):
        with Session(self.engine) as session:
            session.add(Department.to_model(data))
            session.commit()
            return "OK"

    def delete(self, data):
        from sqlalchemy import delete, or_
        with Session(self.engine) as session:
            query = delete(Department).where(or_((Department.id == data.get('id')), (Department.name.ilike(data.get('name')))))
            session.execute(query)
            session.commit()
            return "OK"
    
    def update(self, data):
        with Session(self.engine) as session:
            pass
    
    def get_all(self):
        with Session(self.engine) as session:
            from sqlalchemy import Select

            query = Select(Department)
            result = session.execute(query).fetchall()

            departments = []

            for row in result:
                department = row.tuple()[0]
                departments.append(department.to_json())

            return departments
    
    def get_all_by_employee(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import Select
            query = Select(Department).where(Department.id == data.get('department_id'))
            result = session.execute(query).fetchall()

            departments = []

            for row in result:
                department = row.tuple()[0]
                departments.append(department.to_json())
            
            return departments