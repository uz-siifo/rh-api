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
        
        with Session(self.engine) as session:
            try:
                user = session.query(User).filter(User.id == data.get("id")).first()

                if user:
                    for key, value in data.items():
                        if (hasattr(user, key)):
                            setattr(user, key, value)
                    
                session.commit()
                return user.to_json()
            
            except Exception as e:
                session.rollback()
                return e
            
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
            except Exception as e:
                session.rollback()
                return e

    def get_all(self):
        with Session(self.engine) as session:
            try:
                from sqlalchemy import select
                query = select(User)
                result = session.execute(query).scalars().all()
                users = [user.to_json() for user in result]
                return users
            except Exception as e:
                return e    
        
    def get_by_id(self, data):
        with Session(self.engine) as session:
            try:                
                user = session.query(User).filter(User.id == data.get('id')).first()
                return user.to_json()
            except Exception as e:
                return e

    def get_by_name(self, data):
        with Session(self.engine) as session:
            try:
                from sqlalchemy import Select
                user = session.scalar(
                    Select(User).where(User.name.ilike(data.get('name')))
                )
                return user.to_json() 
            except Exception as e:
                return e
             
    def get_by_username(self, data):
        with Session(self.engine) as session:
            try:
                user = session.query(User).filter(User.username.ilike(data.get("username"))).first()
                return user.to_json()
            except Exception as e:
                return e
            
    def is_user(self, data):
        with Session(self.engine) as session:
            try:
                from sqlalchemy import and_

                admin_user = session.query(User).filter(                    
                    and_(
                        User.username.ilike(data.get("username")),
                        User.passwd.like(data.get("passwd"))
                    )
                ).first()

                return admin_user.to_json()
            except Exception as e:
                return e