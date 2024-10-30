from api.routes.users_contacts_routes import contact_router
from api.routes.users_routes import users_routes
from api.routes.goals_routes import goals_router
from api.routes.performance_evaluation_routes import performance_evaluation_router
from api.routes.presence_routes import presences_router
from api.routes.rating_routes import rating_router
from api.routes.user_employee_routes import user_employee_router
from api.routes.department_routes import department_router
from api.routes.employee_routes import employee_router
from api.routes.progression_routes import progression_router

from fastapi import FastAPI

app = FastAPI()

app.include_router(users_routes)
app.include_router(contact_router)
app.include_router(user_employee_router)
app.include_router(rating_router)
app.include_router(department_router)
app.include_router(goals_router)
app.include_router(presences_router)
app.include_router(performance_evaluation_router)
app.include_router(department_router)
app.include_router(employee_router)
app.include_router(progression_router)