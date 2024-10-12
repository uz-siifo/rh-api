from .service import Service
from model.models import UserContact
from sqlalchemy.orm import Session

class ContactService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        from utils.util import util
        if (util.is_contact(data.get('contact'))):
            with Session(self.engine) as session:
                # contact = UserContact(
                #     user_id = data.get('user_id'),
                #     contact = data.get('contact')
                # )

                session.add(UserContact.to_model(data))
                session.commit()
                return "OK"
                
        return "Contacto Invalido!"
            
    def delete(self, data):
        from sqlalchemy import delete, or_
        with Session(self.engine) as session:
            query = delete(UserContact).where(
                or_(UserContact.id == data.get('id'), UserContact.contact.like(data.get('contact')))
            )
            session.execute(query)
            session.commit()
            return "OK"
        
    def update(self, data):
        from utils.util import util
        if (util.is_contact(data.get('contact'))):
            try:
                from sqlalchemy import update
                with Session(self.engine) as session:
                    stmt = (
                        update(UserContact)
                        .where(UserContact.id == data.get('id'))
                        .values(contact = data.get('contact'))
                    )
                    session.execute(stmt)
                    session.commit()
                    return "OK"
            except Exception as e:
                session.rollback()
                return str(e)
            
        return "Contacto Invalido!"

    def get_all(self):
        with Session(self.engine) as session:
            from sqlalchemy import Select
            query = Select(UserContact)

            result = session.execute(query).fetchall()
            contacts = []

            for row in result:
                contact = row.tuple()[0]
                contacts.append(contact.to_json())

            return contacts

    def get_all_by_user(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import Select

            query = Select(UserContact).where(UserContact.user_id == data.get('user_id'))
            result = session.execute(query).fetchall()
            contacts = []

            for row in result:
                contact = row.tuple()[0]
                contacts.append(contact.to_json())

            return contacts