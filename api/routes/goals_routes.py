from fastapi import APIRouter, Depends, HTTPException, status
from service.goals import GoalsService
from model.models import engine
from auth.auth_service import get_current_user, get_current_admin

goals_router = APIRouter()

@goals_router.get("/goals", summary="List all goals")
async def list_goals(user: str = Depends(get_current_user)):
    """
    Esta rota pode ser acessada por usuários normais para listar as metas.
    """
    service = GoalsService(engine)
    return service.get_all()

@goals_router.post("/goals", summary="Create a new goal")
async def create_goal(data: dict, user: str = Depends(get_current_admin)):
    """
    Apenas gestores podem criar novas metas.
    """
    service = GoalsService(engine)
    return service.create(data)

@goals_router.put("/goals/{goal_id}", summary="Update a goal")
async def update_goal(goal_id: int, data: dict, user: str = Depends(get_current_admin)):
    """
    Apenas gestores podem atualizar as metas.
    """
    service = GoalsService(engine)
    data.update({"id": goal_id})
    return service.update(data)

@goals_router.delete("/goals/{goal_id}", summary="Delete a goal")
async def delete_goal(goal_id: int, user: str = Depends(get_current_admin)):
    """
    Apenas gestores podem deletar as metas.
    """
    service = GoalsService(engine)
    return service.delete({"id": goal_id})

@goals_router.get("/goals/completed", summary="List completed goals by employee")
async def list_completed_goals(employee_id: int, user: str = Depends(get_current_user)):
    """
    Usuários normais podem acessar esta rota para listar as metas concluídas por um funcionário específico.
    """
    service = GoalsService(engine)
    return service.get_completed_goals_by_employee({"employee_id": employee_id})
