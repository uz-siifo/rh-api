from fastapi import APIRouter, Depends
from service.progression import ProgressionService
from model.models import engine
from middlewares.auth import get_current_admin, get_current_user

progression_router = APIRouter()
progression_service = ProgressionService(engine)

@progression_router.get("/admin/progression/", response_model=list)
async def get_all_progression(token:str = Depends(get_current_admin)):
    return progression_service.get_all()

@progression_router.get("/admin/progression/{employee_id}", response_model=list)
async def get_all_progression_by_employee(employee_id: int, token: str = Depends(get_current_admin)):
    return progression_service.get_by_employee_id({"employee_id": employee_id})

@progression_router.get("/progression", response_model=list)
async def get_all_by_user(user: str = Depends(get_current_user)):
    from service.user import UserService
    user_service = UserService(engine)
    user_id = user_service.get_id_by_username({"username": user})
    return progression_service.get_by_employee_id({"employee_id": user_id})