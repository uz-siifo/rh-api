from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Optional
from pydantic import BaseModel
from service.user_employee import UserEmployeeService
from model.models import engine
from middlewares.auth import get_current_admin
from api.base_models.models import UserEmployeeData, UpdateUserEmployeeData

user_employee_router = APIRouter()
user_employee_service = UserEmployeeService(engine)

# Rotas para gerenciamento de usuarios/funcionarios

@user_employee_router.post("/admin/user_employees/create", response_model=str)
async def create_user_employee(data: UserEmployeeData, token: str = Depends(get_current_admin)):
    """
    Criar um novo registro de usuario empregado.
    Apenas usuarios com nivel de acesso de gestor/gerente podem criar registros de usuarios empregados.
    """
    result = user_employee_service.create(data.to_json())
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating user employee")
    
    return result

@user_employee_router.delete("/admin/user_employees/delete", response_model=dict)
async def delete_user_employee(user_employee_id: int, token: str = Depends(get_current_admin)):
    """
    Deletar um registro de usuario empregado especifico.
    Apenas gestores/gerentes podem deletar registros de usuarios empregados.
    """
    result = user_employee_service.delete({"id": user_employee_id})
    if result != {"status": "OK"}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error deleting user employee")
    return result

@user_employee_router.put("/admin/user_employees/update", response_model=dict)
async def update_user_employee(data: UpdateUserEmployeeData, token: str = Depends(get_current_admin)):
    """
    Atualizar um registro de usuario empregado existente.
    Apenas gestores/gerentes podem atualizar registros de usuarios empregados.
    """
    result = user_employee_service.update(data.to_json())
    if result != {"status": "OK"}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error updating user employee")
    return result

@user_employee_router.get("/admin/user_employees/", response_model=list)
async def get_all_user_employees(token: str = Depends(get_current_admin)):
    """
    Listar todos os registros de usuarios empregados.
    Apenas gestores/gerentes podem ver todos os registros de usuarios empregados.
    """
    user_employees = user_employee_service.get_all()
    return user_employees

@user_employee_router.get("/admin/user_employees/employee/", response_model=list)
async def get_all_employees(token: str = Depends(get_current_admin)):
    """
    Listar todos os empregados e suas informacoes associadas.
    Apenas gestores/gerentes podem ver as informacoes de todos os empregados.
    """
    employees = user_employee_service.get_all_employee()
    return employees
