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
from api.routes.router import router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

def main():
    # Permitir CORS para o frontend React (ou outra origem)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # URL do React
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(router)
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

    from datetime import datetime

    if (datetime.now().day == 1):
        from workers.promotion import promoter_worker
        from service.performance_evaluation import PerformanceEvaluationService
        from service.progression import ProgressionService
        from model.models import engine
        performance_evaluation_service = PerformanceEvaluationService(engine)
        progression_service = ProgressionService(engine)
        performance_evaluations = performance_evaluation_service.get_all()
    
        for performance_evaluation in performance_evaluations:

            if (promoter_worker(performance_evaluation)):
                progression_service.create({
                    "employee_id": performance_evaluation.get("employee_id"),
                    "description": "Promovido para programador senior em C++ para robotica e automacao"
                })

if __name__ == "main":
    main()