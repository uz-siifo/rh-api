from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Optional
from pydantic import BaseModel
from service.user_employee import UserEmployeeService
from model.models import engine
from auth.auth_service import get_current_admin

# Inicializando o roteador e o servico
user_employee_router = APIRouter()
user_employee_service = UserEmployeeService(engine)

# Modelos para entrada de dados
class UserEmployeeData(BaseModel):
    user_id: int
    employee_id: int

class UpdateUserEmployeeData(BaseModel):
    id: int
    user_id: Optional[int] = None
    employee_id: Optional[int] = None

# Rotas para gerenciamento de usuarios/funcionarios

@user_employee_router.post("/user_employees/create", response_model=str)
async def create_user_employee(data: UserEmployeeData, token: str = Depends(get_current_admin)):
    """
    Criar um novo registro de usuario empregado.
    Apenas usuarios com nível de acesso de gestor/gerente podem criar registros de usuarios empregados.
    """
    result = user_employee_service.create(data.dict())
    if result != "OK":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating user employee")
    return result

@user_employee_router.delete("/user_employees/delete", response_model=str)
async def delete_user_employee(user_employee_id: int, token: str = Depends(get_current_admin)):
    """
    Deletar um registro de usuario empregado específico.
    Apenas gestores/gerentes podem deletar registros de usuarios empregados.
    """
    result = user_employee_service.delete({"id": user_employee_id})
    if result != "OK":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error deleting user employee")
    return result

@user_employee_router.put("/user_employees/update", response_model=str)
async def update_user_employee(data: UpdateUserEmployeeData, token: str = Depends(get_current_admin)):
    """
    Atualizar um registro de usuario empregado existente.
    Apenas gestores/gerentes podem atualizar registros de usuarios empregados.
    """
    result = user_employee_service.update(data.dict())
    if result != "OK":
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error updating user employee")
    return result

@user_employee_router.get("/user_employees/", response_model=List[Dict[str, str]])
async def get_all_user_employees(token: str = Depends(get_current_admin)):
    """
    Listar todos os registros de usuarios empregados.
    Apenas gestores/gerentes podem ver todos os registros de usuarios empregados.
    """
    user_employees = user_employee_service.get_all()
    return user_employees

@user_employee_router.get("/user_employees/employee/", response_model=List[Dict[str, str]])
async def get_all_employees(token: str = Depends(get_current_admin)):
    """
    Listar todos os empregados e suas informacões associadas.
    Apenas gestores/gerentes podem ver as informacões de todos os empregados.
    """
    employees = user_employee_service.get_all_employee()
    return employees
