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
                # new_user = User(
                #     name = data.get('name'),
                #     nickname = data.get('nickname'),
                #     email = data.get('email'),
                #     passwd = data.get('passwd'),
                #     access_level = data.get('access_level')
                # )
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

                users.append(user.to_json())

            return users
        
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