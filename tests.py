
from model.model import engine
# from sqlalchemy.orm import Session
# from model.department import Department


# from sqlalchemy import select
from service.user import UserService
from service.contacts import ContactService
# from utils.enums import AccessLevelEnum
# user_service = UserService(engine)
contact_service = ContactService(engine)

res = contact_service.delete_by_id({
    "user_id": 16
})

# res = contact_service.create({
#     "user_id": 1,
#     "contact": "+258867640575"
# })


print(res)

# res = user_service.create({
#     "name": "Rene Descartes",
#     "nickname": "Muala",
#     "email": "rende.muala@icloud.com",
#     "passwd": "10134456",
#     "access_level": 'user',
#     "contact": "+258831780781"
# })

# print(res)

# with Session(engine) as session:
#     result = session.scalar(
#         select(Department)
#     )

#     print(result.name)


# from model.user import User
# with Session(engine) as session:
#     from utils.enums import AccessLevelEnum
#     result = session.scalar(
#         select(User).where(User.access_level == AccessLevelEnum.admin)
#     )

#     print(result.name)
#     user = User(
#         name = "Eloide Simao",
#         nickname = "Novela",
#         email = "eloide@outlook.com",
#         passwd = "10134456",
#         access_level = AccessLevelEnum.admin
#     )

#     from model.user_contact import UserContact
#     _contact = UserContact(contact="+258867640575")
#     user.contacts = [_contact] 

#     session.add(user)
#     session.commit()
# select_user()