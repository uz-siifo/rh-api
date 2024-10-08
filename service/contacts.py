from .service import Service
from model.user_contact import UserContact
from sqlalchemy.orm import Session
# from sqlalchemy import select
from sqlalchemy import delete

class ContactService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        with Session(self.engine) as session:
            contact = UserContact(
                user_id = data.get('user_id'),
                contact = data.get('contact')
            )

            session.add(contact)
            session.commit()
            return "OK"

    def delete_by_id(self, data):
        with Session(self.engine) as session:
            try:
                query = delete(UserContact).where(UserContact.user_id == data.get('user_id'))
                session.execute(query)
                session.commit()
                return "OK"
            except Exception as e:
                session.rollback()
                return str(e)

    def delete_by_contact(self, data):
        with Session(self.engine) as session:
            try:
                query = delete(UserContact).where(UserContact.contact == data.get('contact'))
                session.execute(query)
                session.commit()
                return "OK"
            except Exception as e:
                session.rollback()
                return str(e)

    def update(self, data):
        with Session(self.engine) as session:
            pass

    def get_all(self):
        with Session(self.engine) as session:
            pass

    def get_all_by_user(self, data):
        with Session(self.engine) as session:
            pass