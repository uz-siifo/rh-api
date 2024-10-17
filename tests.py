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

# print(user_employee_service.create({
#     "user_id": 3,
#     "employee_id": 1
# }))

# print(user_service.create({
#     "name": "Eloide Simao",
#     "nickname": "Novela",
#     "email": "eloide.novela@outlook.com",
#     "passwd": "10134456",
#     "username": "eloide-novela",
#     "access_level": "admin",
#     "contact": "+258876545335"
# }))

# from datetime import datetime
# print(employee_service.create({
#     'position_at_work': "engineer",
#     'nuit': 29393919,
#     'identity_card_bi': "387437754763767A2",
#     'salary': 199292.091,
#     'date_admission': datetime.now(),
#     'academic_level': "higher",
#     'department_id': 1
# }))

print("user_serive: ", user_service.get_all(), "\n\n\n")

# print(user_service.is_admin("eloide-novela"))
# print(user_service.create({
#      "name": "Eloide Simao",
#      "username": "eloide-novela",
#      "nickname": "Novela",
#     "email": "eloide.novela@outlook.com",
#     "passwd": "1013eloide.novela",
#     "access_level": "admin",
#     "contact": "+258876545335"
# }))

# print("employee_service: ", employee_service.get_all(), "\n\n\n")
# print("contact_service: ", contact_service.get_all(), "\n\n\n")
# print("department_service: ", department_service.get_all(), "\n\n\n")
# print("employee_rating_service: ", employee_rating_service.get_all(), "\n\n\n")
# print("goals_service: ", goals_service.get_all(), "\n\n\n")
# print("month_records_service: ", month_records_service.get_all(), "\n\n\n")
# print("performance_evaluation_service: ", performance_evaluation_service.get_all(), "\n\n\n")
# print("presences_service: ", presences_service.get_all(), "\n\n\n")
# print("user_employee_service: ", user_employee_service.get_all_employee(), "\n\n\n")
# print("working_hours_service: ", working_hours_service.get_all(), "\n\n\n")

# # print(user_service.is_user({
# #     "username": "eloide-novela",
# #     "passwd": "1013eloide.novela"
# # }))
# # from model.models import *

# # print(goals_service.get_completed_goals_by_employee({
# #     "employee_id": 1
# # }))
