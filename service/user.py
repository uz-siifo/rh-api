from .service import Service
from model.models import User, UserContact
from sqlalchemy.orm import Session
from sqlalchemy import select

class UserService(Service):

    """
    Servico para manipulacao de usuarios.

    Metodos:
    - create(data): Cria um novo usuario e adiciona ao banco de dados.
    - update(data): Atualiza os dados de um usuario existente.
    - delete(data): Remove um usuario do banco de dados.
    - get_all(): Retorna todos os usuarios cadastrados.
    - is_user(data): Verifica se um usuario existe com base em nome de usuario e senha.
    - get_by_id(data): Retorna os dados de um usuario com base em seu ID.
    - get_by_name(data): Retorna os dados de um usuario com base em seu nome.
    - is_admin(username): Verifica se um usuario tem nivel de acesso admin.

    Atributos:
    - engine: Instancia do banco de dados utilizada para realizar as operacoes.
    """

    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                from utils.util import util
                if (util.is_email(data.get("email"))):
                    new_user = User.to_model(data)
                    contact = UserContact(contact=data.get('contact'))
                    new_user.contacts = [contact]

                    session.add(new_user)
                    session.commit()
                    return "OK"
                
        except Exception as e:
            return str(e)           

    def update(self, data):
        from sqlalchemy import update
        with Session(self.engine) as session:
            stmt = (
                update(User)
                .where(User.id == data.get('id'))
                .values(contact = data.get('contact'))
            )
            session.execute(stmt)
            session.commit()
            return "OK"

    def delete(self, data):
        from sqlalchemy import delete, or_
        with Session(self.engine) as session:
            query = delete(User).where(
                or_(
                    User.id == data.get('id'), 
                    User.email.like(data.get('email')),
                )
            )

            session.execute(query)
            session.commit()
            return "OK"

    def get_all(self):
        with Session(self.engine) as session:
            from sqlalchemy import select
            query = select(User)

            result = session.execute(query).fetchall()
            users = []

            for row in result:
                user = row.tuple()[0]

                users.append(user.to_json())

            return users
    
    def is_user(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import select, and_
            query = select(User).where(and_(
                User.username == data.get("username"),
                User.passwd == data.get("passwd")
            ))

            res = session.execute(query).first()
            
            return res is not None
        
    def get_by_id(self, data):
        with Session(self.engine) as session:
            user = session.scalar(
                select(User).where(User.id == data.get('id'))
            )

            return user.to_json()

    def get_by_name(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import Select
            user = session.scalar(
                Select(User).where(User.name == data.get('name'))
            )

            return user.to_json() 
        
    def is_admin(self, username):
        with Session(self.engine) as session:
            from sqlalchemy import select, and_
            from utils.enums import AccessLevelEnum

            query = select(User).where(and_(
                User.username.ilike(username),
                User.access_level == AccessLevelEnum.admin
            ))

            result = session.execute(query).fetchall()

            return len(result) > 0