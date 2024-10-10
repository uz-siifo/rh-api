
# from model.model import *

from model.model import engine
# from sqlalchemy.orm import Session
# from model.department import Department


# from sqlalchemy import select
from service.user import UserService
from service.contacts import ContactService
from service.department import DepartmentService
from service.employee import EmployeeService
from service.user_employee import UserEmployeeService
# from model.employee import Employee
from model.employee_rating import EmployeeRating
# from utils.enums import AccessLevelEnum
user_service = UserService(engine)

print(user_service.get_all())
# user_employee_service = UserEmployeeService(engine)
# print(user_employee_service.create({
#     "user_id": 2,
#     "employee_id": 1
# }))

# print(user_employee_service.get_all())
# employee_service = EmployeeService(engine)
# print(employee_service.get_all())

            # employee = Employee(
            #     nuit = data.get('nuit'),
            #     identity_card_bi = data.get('identity_card_bi'),
            #     salary = data.get('salary'),
            #     data_admission = data.get('data_admission'),
            #     department_id = data.get('department_id'),
            #     academic_level = data.get('academic_level')
            # )

# from datetime import date
# print(employee_service.create({
#     "nuit": 10101010,
#     "identity_card_bi": "7774484848S988",
#     "salary": 101092.2,
#     "data_admission": date.fromisoformat('2019-12-04'),
#     "department_id": 1
# }))

# contact_service = ContactService(engine)

# dept_service = DepartmentService(engine)
# # print(dept_service.delete({
# #     "name": "Medicina"
# # }))

# print(dept_service.get_all())

# print(dept_service.create({
#         "name": "Medicina",
#         "employee_nums": 10,
#         "min_salary": 1000.8,
#         "max_salary": 16000.18
#     })
# )
# res = contact_service.get_all()
# print(res)

# res = contact_service.get_all_by_user({
#     "user_id": 3
# })

# print(res)
# res = contact_service.delete_by_id({
#     "user_id": 16
# })

# creating contact
# res = contact_service.create({
#     "user_id": 1,
#     "contact": "+258867640575"
# })


# updating contact
# res = contact_service.update({
#     "id": 2,
#     "contact": "+258876545439"
# })

# print(res)

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