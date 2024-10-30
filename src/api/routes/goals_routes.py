from fastapi import APIRouter, Depends, HTTPException, status
from service.goals import GoalsService
from model.models import engine
from middlewares.auth import get_current_user, get_current_admin
from api.base_models.models import GoalsData, UpdateGoalsData

goals_router = APIRouter()

@goals_router.post("/admin/goals", response_model = dict)
async def create_goal(data: GoalsData, user: str = Depends(get_current_admin)):
    """
    Apenas gestores podem criar novas metas.
    """
    service = GoalsService(engine)
    result = service.create(data.to_json())

    if (isinstance(result, Exception)):
        return {"Error": str(result)}
    
    return result

@goals_router.put("/admin/goals/{goal_id}", response_model=dict)
async def update_goal(data: UpdateGoalsData, user: str = Depends(get_current_admin)):
    """
    Apenas gestores podem atualizar as metas.
    """
    service = GoalsService(engine)
    result = service.update(data.to_json())  
    if (isinstance(result, Exception)):
        return {"Error": str(result)}
    
    return result


@goals_router.delete("/admin/goals/{goal_id}", response_model=dict)
async def delete_goal(goal_id: int, user: str = Depends(get_current_admin)):
    """
    Apenas gestores podem deletar as metas.
    """
    service = GoalsService(engine)
    result = service.delete({"id": goal_id})
    if (isinstance(result, Exception)):
        return {"Error": str(result)}

    return result

@goals_router.get("/admin/goals/completed", response_model=list)
async def list_completed_goals(user: str = Depends(get_current_admin)):
    """
    Usuarios normais podem acessar esta rota para listar as metas concluidas por um funcionario especifico.
    """
    from service.user import UserService
    user_service = UserService(engine)
    id = user_service.get_id_by_username({"username": user})
    service = GoalsService(engine)

    return service.get_completed_goals_by_employee({"employee_id": id})

@goals_router.get("/goals", response_model=list)
async def list_goals(user: str = Depends(get_current_user)):
    """
    Esta rota pode ser acessada por um usuario normail para listar suas metas.
    """
    from service.user import UserService
    user_service = UserService(engine)
    id = user_service.get_id_by_username({"username": user})
    service = GoalsService(engine)

    return service.get_all_goals_by_employee({"employee_id": id})
