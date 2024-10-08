# from db.connect import conn, cur
from .service import Service
from model.user import User
from sqlalchemy.orm import Session
from sqlalchemy import select
from model.user_contact import UserContact

class UserService(Service):

    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_user = User(
                    name = data.get('name'),
                    nickname = data.get('nickname'),
                    email = data.get('email'),
                    passwd = data.get('passwd'),
                    access_level = data.get('access_level')
                )

                contact = UserContact(contact=data.get('contact'))
                new_user.contacts = [contact]

                session.add(new_user)
                session.commit()
                return {"OK"}
        except Exception as e:
            return str(e)           

    def update(self, data):
        with Session(self.engine) as session:
            pass

    def delete(self, data):
        with Session(self.engine) as session:
           pass 

    def get_all(self):
        with Session(self.engine) as session:
            from sqlalchemy import Select
            query = Select(User)

            result = session.execute(query).fetchall()
            users = []

            for row in result:
                user = row.tuple()[0]

                users.append({
                    "id": user.id,
                    "name": user.name,
                    "nickname": user.nickname,
                    "email": user.email,
                    "passwd": user.passwd,
                    "access_level": user.access_level,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at
                })

            return users
        
    def get_by_id(self, data):
        with Session(self.engine) as session:
            return session.scalar(
                select(User).where(User.id == data.get('id'))
            )

    def get_by_name(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import Select
            return session.scalar(
                Select(User).where(User.name == data.get('name'))
            )