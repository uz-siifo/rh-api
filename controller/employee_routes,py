from service.employee import EmployeeService
from typing import Dict
from auth.auth_service import get_current_user, get_current_admin
from model.models import engine
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from typing import List
# Definindo a API Router para os funcionários
employee_router = APIRouter()
employee_service = EmployeeService(engine)

class EmployeeData(BaseModel):
    name: str
    identity_card_bi: str
    position: str
    department: str

class UpdateEmployeeData(BaseModel):
    id: int
    name: str = None
    identity_card_bi: str = None
    position: str = None
    department: str = None

@employee_router.post("/employees/create", response_model=str)
async def create_employee(data: EmployeeData, token: str = Depends(get_current_admin)):
    """
    Criar um novo funcionário.
    Apenas usuários com nível de acesso de gestor/gerente podem criar novos funcionários.
    """
    return employee_service.create(data.dict())

@employee_router.put("/employees/update", response_model=str)
async def update_employee(data: UpdateEmployeeData, token: str = Depends(get_current_admin)):
    """
    Atualizar informações de um funcionário.
    Apenas usuários com nível de acesso de gestor/gerente podem atualizar os detalhes dos funcionários.
    """
    return employee_service.update(data.dict())

@employee_router.delete("/employees/delete", response_model=str)
async def delete_employee(data: Dict[str, str], token: str = Depends(get_current_admin)):
    """
    Deletar um funcionário específico.
    Apenas usuários com nível de acesso de gestor/gerente podem deletar funcionários.
    """
    return employee_service.delete(data)

@employee_router.get("/employees/", response_model=List[Dict[str, str]])
async def get_all_employees(token: str = Depends(get_current_admin)):
    """
    Listar todos os funcionários.
    Apenas usuários com nível de acesso de gestor/gerente podem visualizar a lista completa de funcionários.
    """
    return employee_service.get_all()

