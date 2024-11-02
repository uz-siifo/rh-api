from .service import Service
from sqlalchemy.orm import Session
from model.models import UserEmployee

class UserEmployeeService(Service):
    """
    Servico para manipulacao de usuarios empregados.

    Metodos:
    - create(data): Cria um novo usuario empregado e adiciona ao banco de dados.
    - delete(data): Remove um usuario empregado do banco de dados.
    - update(data): Atualiza os dados de um usuario empregado existente.
    - get_all(): Retorna todos os usuarios empregados cadastrados.
    - get_all_employee(): Retorna informacoes detalhadas de todos os empregados.

    Atributos:
    - engine: Instancia do banco de dados utilizada para realizar as operacoes.
    """
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        with Session(self.engine) as session:
            try:
                user_employee = UserEmployee.to_model(data)
                session.add(user_employee)
                session.commit()
                return user_employee.to_json()
            except Exception as error:
                session.rollback()
                return error
                    
    def delete(self, data):
        from sqlalchemy import delete
        with Session(self.engine) as session:
            try:
                query = delete(UserEmployee).where(UserEmployee.id == data.get('id'))
                session.execute(query)
                session.commit()
                return {"status": "OK"}

            except Exception as error:
                session.rollback()
                return error

    def update(self, data):
        with Session(self.engine) as session:
            try:
                user_employee = session.query(UserEmployee).filter(UserEmployee.id == data.get("id")).first()
                for key, value in data.items():
                    if (hasattr(user_employee, key)):
                        setattr(user_employee, key, value)
                session.commit()
                return user_employee.to_json()
            except Exception as error:
                session.rollback()
                return str(error)

    def get_all(self):
        from sqlalchemy import Select
        with Session(self.engine) as session:
            query = Select(UserEmployee)
            result = session.execute(query).scalars().all()
            user_employees = [user_employee.to_json() for user_employee in result]
            return user_employees
        
    def get_all_employee(self):
        with Session(self.engine) as session:
            from sqlalchemy import select, and_
            from model.models import User, Employee, Department
            query = select(
                User.name, 
                User.nickname, 
                User.email,  
                Employee.identity_card_bi, 
                Employee.nuit,
                Employee.position_at_work
            ).where(
                and_(
                    User.id == UserEmployee.user_id,
                    Employee.id == UserEmployee.employee_id
                )
            )

            result = session.execute(query).fetchall()
            employee = {}

            for row in result:

                employee = {
                    "name": row[0],
                    "nickname": row[1],
                    "email": row[2],
                    "identity_card_bi": row[3],
                    "nuit": row[4],
                    "position_at_work": row[5].get_value()
                }

            return employee