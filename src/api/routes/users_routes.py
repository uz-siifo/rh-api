from middlewares.auth import *
from service.user import UserService
from model.models import engine
from fastapi import APIRouter


users_routes = APIRouter()
user_service = UserService(engine)

from api.base_models.models import UserData
from api.base_models.models import EmployeeData

@users_routes.post("/admin/users/create", response_model=dict)
async def create_user(user_data: UserData, employee_data: EmployeeData, token: str = Depends(get_current_admin)):
    from service.employee import EmployeeService
    employee_service = EmployeeService(engine)
    result = employee_service.create(employee_data.to_json(), user_data.to_json())
    if isinstance(result, Exception):
        return {"Erro": str(result)}
    
    return result

"""
    rota para atualizar inforcamacoes dos usuarios, esta rota e restrita apenas o admin do sistema
    Tem uma dependecia! 
"""
@users_routes.put("/admin/users/update", response_model=dict)
async def update_user(data: UserData, token: str = Depends(get_current_admin)):
    result = user_service.update(data.to_json())

    if isinstance(result, Exception):
        return  {"Error": str(result)}
    
    return result

@users_routes.delete("/admin/users/delete", response_model=dict)
async def delete_user(data: dict, token: str = Depends(get_current_admin)):

    result = user_service.delete(data)

    if isinstance(result, Exception):
        return {"Error": str(result)}
    
    return result

@users_routes.get("/admin/users/", response_model=List[dict])
async def get_all_users(token: str = Depends(get_current_admin)):
    return user_service.get_all()

@users_routes.get("/users/{user_id}", response_model=dict)
async def get_user_by_id(user_id: int, token: str = Depends(get_current_user)):
    return user_service.get_by_id({"id": user_id})

@users_routes.get("/users/by-name/{name}", response_model=dict)
async def get_user_by_name(name: str, token: str = Depends(get_current_user)):
    return user_service.get_by_name({"name": name})
