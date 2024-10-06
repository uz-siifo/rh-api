
from model.model import *
from sqlalchemy.orm import Session
from model.user import User
from model.user_contact import UserContact
from utils.enums import AccessLevelEnum
from sqlalchemy import select


with Session(engine) as session:
    result = session.scalar(
        select(User).where(User.id == 1)
    )

    print(result.name)
    # user = User(
    #     name = "Eloide Simao",
    #     nickname = "Novela",
    #     email = "eloide.simao@outlook.com",
    #     passwd = "10134456",
    #     access_level = AccessLevelEnum.admin
    # )

    # _contact = UserContact(contact="+258867640575")
    # user.contacts = [_contact] 

    # session.add(user)
    # session.commit()
# select_user()