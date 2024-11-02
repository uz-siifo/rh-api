from service.employee import EmployeeService
from service.user import UserService
from service.contacts import ContactService
from service.department  import DepartmentService
from service.employee_rating import EmployeeRatingService
from service.goals import GoalsService
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
performance_evaluation_service = PerformanceEvaluationService(engine)
presences_service = PresencesService(engine)
user_employee_service = UserEmployeeService(engine)
working_hours_service = WorkingHoursService(engine)
# print(employee_service.create({

#     "name": "Eloide",
#     "nickname": "Novela",
#     "username": "eloide-novela",
#     "email": "eloide.novela@gmail.com",
#     "passwd": "10134456",
#     "role": "user",
#     "position": "engineer",
#     "state":"active",
#     "length_of_service": 1,
#     "date_admission": "2024-11-11",
#     'academic_level': "Mestre",
#     "department": "Informatica"
# }))


# from model.models import get_storage

# get_storage()
# print(user_service.get_all())

# print(employee_rating_service.get_all())
# print(performance_evaluation_service.get_all_())
# print(user_employee_service.get_all_empl
#oyee())

# print(type)


# from utils.enums import PositionAtWorkEnum

# pos = PositionAtWorkEnum("engineer")

# print(pos.value)
# print(employee_service.get_all())
# print(contact_service.get_all_by_user({"user_id": 1}))
# from model.models import Employee
# from datetime import datetime
# from model.models import *

# numbers = [number for number in [9, 5, 4, 2]]

# print(employee_service.get_all())
# print(employee_service.get_all_by_department({"department_id": 1}))
# print(contact_service.get_all())
# print(presences_service.get_all())
# print(numbers)
# employee = Employee()

# print(employee_service.create({
#     'position_at_work': "engineer",
#     # 'nuit': 293939197,
#     'identity_card_bi': "383437754363767A2",
#     # 'salary': 199292.091,
#     'date_admission': datetime.now(),
#     'academic_level': "higher",
#     'department_id': 1,
#     "age": 65,
#     "length_of_service": 10
# },
# {
#     "name": "Simao Pedro",
#     "nickname": "Novela",
#     "email": "simao.novela@gmail.com",
#     "contact": "+258846937430",
#     "username": "simao-pedro",
#     "passwd": "10134456879",
#     "role": "user"
# }))


# print(contact_service.create({
#     "user_id": 1,
#     "contact": "+258846937430"
# }))

# print(department_service.create({
#     "name": "Informatica",
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
#     "role": "user",
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
#     "role": "user",
#     "contact": "+258876548336"
# }

# for key in ad.keys():

#     print(key)

# from model.models import get_storage

# get_storage()


# print(user_service.is_user({"username": "elda-novela", "passwd": "56441310"}))

# print(user_service.create({
#     "name": "Eloid Simao",
#     "nickname": "Novela",
#     "email": "eloid.novela@outlook.com",
#     "passwd": "56441310",
#     "username": "eloid-novela",
#     "role": "user",
#     "contact": "+258867640575"
# }))

# print(user_service.get_all())

# print(user_service.update({
#     "nickname": "_chume",
#     "id": 3
# }))

# print({"nome": "Eloide"} == {"nom": "Eloide"})

# print(user_service.get_by_id({"id": 3}))
# a = KeyError()

# print(isinstance(a, KeyError) )

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

print(user_service.is_user({"username": "josias-magumba"}))
# print(user_service.create({
#      "name": "Eloide Simao",
#      "username": "eloide-novela",
#      "nickname": "Novela",
#     "email": "eloide.novela@outlook.com",
#     "passwd": "1013eloide.novela",
#     "role": "admin",
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


# import jwt

# key = "sifo-senha-secreta"

# encoded = jwt.encode({
#   "token_de_acesso": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlbGRhLW5vdmVsYSIsImV4cCI6MTcyOTc5Mjc5OH0.rGqx-9OmX1iIttcqTPkzITcKRYtXfJmE9l5InaDuKgM",
#   "tipo_de_token": "bearer"
# }, key, algorithm="HS256")
# print(encoded)
# decoded = jwt.decode(encoded, key, algorithms="HS256")
# # {'some': 'payload'}

# print(decoded.get("tipo_de_token"))



#  "is_assiduous": performance_evaluation[0],
#                     "is_collaborative": performance_evaluation[1],
#                     "completed_goals": performance_evaluation[2],
#                     "is_punctual": performance_evaluation[3], 
#                     "presences": performance_evaluation[4],
#                     "absences": performance_evaluation[5],
#                     "work_quality_rating": performance_evaluation[6],
#                     "problem_solving_skills_rating": performance_evaluation[7],
#                     "communication_skills_rating": performance_evaluation[8],
#                     "time_management_skills_rating": performance_evaluation[9],
#                     "leadership_skills_rating": performance_evaluation[10]

# dados = performance_evaluation_service.get_all()[0]

# di = {}

# di.update({"name": "eloid"})

# print(di)

# print(dados)
# from workers.promotion import promoter_worker

# print(promoter_worker(dados))


# arr = {"a": 8, "b": 5,"c":  4,"d":  3,"e":  1}
# a = arr.values()
# for key in arr.keys():
#     print(key)
# print(arr.keys()[0])
# print(performance_evaluation_service.get_all())

# from threading import Thread


# user = {
#     "id": 1,
#     "name": "Josias",
#     "username": "josias-magumba",
#     "nickname": "Magumba",
#     "email": "josias.magumba@outlook.com",
#     "passwd": "magumba"
#     # "role": "admin",
#     # "contact": "+258867640575"
# }

# print(user_service.update(user))

# for key, value in user.items():
#     print(key, value)

# aux_user = {}
# for key in user.keys():

#     aux_user.update({key: user.get(key)})

# print(aux_user)

# print(user_service.get_all())