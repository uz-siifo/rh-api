from .service import Service
from model.models import UserContact
from sqlalchemy.orm import Session
from utils.util import util

class ContactService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        from utils.util import util
        if (util.is_contact(data.get('contact'))):
            with Session(self.engine) as session:
                try:
                    new_contact = UserContact.to_model(data)
                    session.add(new_contact)
                    session.commit()
                    return new_contact.to_json()
                except Exception as error:
                    session.rollback()
                    return error
                
        return "Contacto Invalido!"
            
    def delete(self, data):
        from sqlalchemy import delete, or_
        with Session(self.engine) as session:
            try:
                query = delete(UserContact).where(
                    or_(
                        UserContact.id == data.get('id'), 
                        UserContact.contact.like(data.get('contact'))
                    )
                )
                session.execute(query)
                session.commit()
                return {"Status": "OK"}
            except Exception as error:
                session.rollback()
                return error
        
    def update(self, data):
        from utils.util import util
        if (util.is_contact(data.get('contact'))):
            try:
                with Session(self.engine) as session:

                    contact = session.query(UserContact).filter(UserContact.id == data.get("id")).first()
                    for key, value in data.items():
                        if (hasattr(contact, key)):
                            setattr(contact, key, value)
                    session.commit()
                    return contact.to_json()
            except Exception as error:
                session.rollback()
                return error
            
        return "Contacto Invalido!"

    def get_all(self):
        with Session(self.engine) as session:
            from sqlalchemy import Select
            query = Select(UserContact)
            result = session.execute(query).scalars().all()
            contacts = [contact.to_json() for contact in result]
            return contacts

    def get_all_by_user(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import Select
            query = Select(UserContact).where(UserContact.user_id == data.get('user_id'))
            result = session.execute(query).fetchall()
            contacts = [contact.tuple()[0].to_json() for contact in result]
            return contacts