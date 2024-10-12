from .service import Service
from model.models import User, UserContact
from sqlalchemy.orm import Session
from sqlalchemy import select

class UserService(Service):

    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
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