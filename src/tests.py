from service.employee import EmployeeService
from service.user import UserService
from service.contacts import ContactService
from service.department  import DepartmentService
from service.employee_rating import EmployeeRatingService
from service.goals import GoalsService
from service.month_records import MonthRecordsService
from service.performance_evaluation import PerformanceEvaluationService
from service.presences import PresencesService
from service.user_employee import UserEmployeeService
from service.working_hours import WorkingHoursService
from model.models import engine

employee_service = EmployeeService(engine)
user_service = UserService(engine)
contact_service = ContactService(engine)
department_service = DepartmentService(engine)
employee_rating_service = EmployeeRatingService(engine)
goals_service = GoalsService(engine)
month_records_service = MonthRecordsService(engine)
performance_evaluation_service = PerformanceEvaluationService(engine)
presences_service = PresencesService(engine)
user_employee_service = UserEmployeeService(engine)
working_hours_service = WorkingHoursService(engine)

# print(department_service.create({
#     "name": "Informatica",
#     "employee_nums": 10,
#     "min_salary": 189893,
#     "max_salary": 29299292
# }))
# from datetime import datetime
# print(employee_service.create({
#     'position_at_work': "engineer",
#     'nuit': 293939198,
#     'identity_card_bi': "387437754363767A2",
#     'salary': 199292.091,
#     'date_admission': datetime.now(),
#     'academic_level': "higher",
#     'department_id': 1

# }, 
# {
#     "name": "Emmanuel Michaque",
#     "nickname": "Novela",
#     "email": "emmanuel.sibanda@outlook.com",
#     "passwd": "10134456",
#     "username": "emmanuel-sibanda",
#     "access_level": "user",
#     "contact": "+258876454833"

# }))


# print(user_service.update({"id": 10, "nickname": "Sibanda"}))
# print(contact_service.get_all())

# print(user_service.get_all())
# print(department_service.get_by_id({"id": 1}))

# # print(user_ecle mployee_service.create({
# #     "user_id": 3,
# #     "employee_id": 1
# # }))

# ad = {
#     "name": "Eleuterio Simao",
#     "nickname": "Novela",
#     "email": "eleuterio.novela@outlook.com",
#     "passwd": "10134456",
#     "username": "eleuterio-novela",
#     "access_level": "user",
#     "contact": "+258876548336"
# }

# for key in ad.keys():

#     print(key)

# print(user_service.create({
#     "name": "Elda Simao",
#     "nickname": "Novela",
#     "email": "elda.novela@outlook.com",
#     "passwd": "56441310",
#     "username": "elda-novela",
#     "access_level": "admin",
#     "contact": "+258876548339"
# }))

# # from datetime import datetime
# # print(employee_service.create({
# #     'position_at_work': "engineer",
# #     'nuit': 29393919,
# #     'identity_card_bi': "387437754763767A2",
# #     'salary': 199292.091,
# #     'date_admission': datetime.now(),
# #     'academic_level': "higher",
# #     'department_id': 1
# # }))

# print(user_service.delete({"id": 8}))

# print("user_serive: ", user_service.get_all(), "\n\n\n")

# # print(user_service.is_admin("eloide-novela"))
# print(user_service.create({
#      "name": "Eloide Simao",
#      "username": "eloide-novela",
#      "nickname": "Novela",
#     "email": "eloide.novela@outlook.com",
#     "passwd": "1013eloide.novela",
#     "access_level": "admin",
#     "contact": "+258867640575"
# }))

# # print("employee_service: ", employee_service.get_all(), "\n\n\n")
# # print("contact_service: ", contact_service.get_all(), "\n\n\n")
# # print("department_service: ", department_service.get_all(), "\n\n\n")
# # print("employee_rating_service: ", employee_rating_service.get_all(), "\n\n\n")
# # print("goals_service: ", goals_service.get_all(), "\n\n\n")
# # print("month_records_service: ", month_records_service.get_all(), "\n\n\n")
# # print("performance_evaluation_service: ", performance_evaluation_service.get_all(), "\n\n\n")
# # print("presences_service: ", presences_service.get_all(), "\n\n\n")
# # print("user_employee_service: ", user_employee_service.get_all_employee(), "\n\n\n")
# # print("working_hours_service: ", working_hours_service.get_all(), "\n\n\n")

# # # print(user_service.is_user({
# # #     "username": "eloide-novela",
# # #     "passwd": "1013eloide.novela"
# # # }))
# # # from model.models import *

# # # print(goals_service.get_completed_goals_by_employee({
# # #     "employee_id": 1
# # # }))

# from model.models import Progression


import jwt

key = "sifo-senha-secreta"

encoded = jwt.encode({
  "token_de_acesso": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlbGRhLW5vdmVsYSIsImV4cCI6MTcyOTc5Mjc5OH0.rGqx-9OmX1iIttcqTPkzITcKRYtXfJmE9l5InaDuKgM",
  "tipo_de_token": "bearer"
}, key, algorithm="HS256")
print(encoded)
decoded = jwt.decode(encoded, key, algorithms="HS256")
# {'some': 'payload'}

print(decoded.get("tipo_de_token"))