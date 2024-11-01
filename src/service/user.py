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
        with Session(self.engine) as session:
            try:
                from utils.util import util
                if (util.is_email(data.get("email"))):
                    new_user = User.to_model(data)
                    contact = UserContact(contact=data.get('contact'))
                    new_user.contacts = [contact]
                    session.add(new_user)
                    session.commit()
                    return new_user.to_json()
            except Exception as ex:
                session.rollback()
                return ex        

    def update(self, data):
        
        from sqlalchemy import update
        with Session(self.engine) as session:
            try:
                stmt = (
                    update(User)
                    .where(User.id == data.get('id'))
                    .values(nickname = data.get("nickname"))
                )
                session.execute(stmt)
                session.commit()
                return {"Status": "OK"}
            
            except Exception as error:
                session.rollback()
                return error
            
    def delete(self, data):
        from sqlalchemy import delete, or_
        with Session(self.engine) as session:
            try:
                query = None
                if data.get("email") is not None:

                    query = delete(User).where(
                        or_(
                            User.email.like(data.get('email')),
                        )
                    )
                elif data.get("id") is not None:
                    query = delete(User).where(
                        or_(
                            User.id == data.get('id')
                        )
                    )

                session.execute(query)
                session.commit()
                return {"status": "OK"}
            except Exception as error:
                session.rollback()
                return error

    def get_all(self):
        with Session(self.engine) as session:
            from sqlalchemy import select
            query = select(User)

            result = session.execute(query).scalars().all()
            users = [user.to_json() for user in result]
            return users
    
    def is_user(self, data):
        with Session(self.engine) as session:
            try:
                from sqlalchemy import select, and_
                query = select(User).where(and_(
                    User.username == data.get("username"),
                    User.passwd == data.get("passwd")
                ))

                res = session.execute(query).fetchone()
                
                return res.tuple()[0].to_json()
            except Exception as e:
                return e
        
    def get_by_id(self, data):
        with Session(self.engine) as session:
            try:
                user = session.scalar(
                select(User).where(User.id == data.get('id'))
                )

                return user.to_json()
            except Exception as e:
                return e

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
    def get_id_by_username(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import select
            query = select(User.id).where(
                User.username.ilike(data.get("username"))
            )

            result = session.execute(query).fetchone()

            return result.tuple()[0]