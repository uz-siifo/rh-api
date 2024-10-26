from service.service import Service
from sqlalchemy.orm import Session
from model.models import Department

class DepartmentService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)
    
    def create(self, data):
        with Session(self.engine) as session:
            try:
                new_department = Department.to_model(data)
                session.add(new_department)
                session.commit()
                return new_department.to_json()
            except Exception as error:
                session.rollback()
                return str(error)
            
    def delete(self, data):
        from sqlalchemy import delete, or_
        with Session(self.engine) as session:
            try:
                query = delete(Department).where(or_((Department.id == data.get('id')), (Department.name.ilike(data.get('name')))))
                session.execute(query)
                session.commit()
                return "OK"
            except Exception as error:
                session.rollback()
                return str(error)
            
    def update(self, data):
        from sqlalchemy import update
        with Session(self.engine) as session:
            try:    
                new_department = Department.to_model(data)
                session.query(Department).filter(Department.id == data.get('id')).update(
                    new_department.to_json()
                )

                session.commit()
                return new_department.to_json()
            except Exception as error:
                session.rollback()
                return str(error)

    def get_all(self):
        with Session(self.engine) as session:
            from sqlalchemy import Select
            query = Select(Department)
            result = session.execute(query).fetchall()
            departments = [department.tuple()[0].to_json() for department in result]
            return departments
        
    def get_by_id(self, data):
        try:
            with Session(self.engine) as session:
                from sqlalchemy import select
                query = select(Department).where(Department.id == data.get("id"))
                department = session.execute(query).fetchone().tuple()[0]
                return department.to_json()
             
        except Exception as e:
            return str(e)
    
    def get_all_by_employee(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import Select
            query = Select(Department).where(Department.id == data.get('department_id'))
            result = session.execute(query).fetchall()
            departments = [department.tuple()[0].to_json() for department in result]  
            return departments