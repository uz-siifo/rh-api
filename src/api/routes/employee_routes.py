from service.employee import EmployeeService
from typing import Dict
from auth.auth_service import get_current_user, get_current_admin
from model.models import engine
from fastapi import APIRouter, Depends
from pydantic import BaseModel

from typing import List
# Definindo a API Router para os funcionarios
employee_router = APIRouter()
employee_service = EmployeeService(engine)

from api.base_models.models import UserData
from api.base_models.models import EmployeeData, UpdateEmployeeData


@employee_router.post("/employees/create", response_model=str)
async def create_employee(employee: EmployeeData, user: UserData, token: str = Depends(get_current_admin)):
    """
    Criar um novo funcionario.
    Apenas usuarios com nivel de acesso de gestor/gerente podem criar novos funcionarios.
    """
    return employee_service.create(employee.to_json(), user.to_json())

@employee_router.put("/employees/update", response_model=str)
async def update_employee(data: UpdateEmployeeData, token: str = Depends(get_current_admin)):
    """
    Atualizar informações de um funcionario.
    Apenas usuarios com nivel de acesso de gestor/gerente podem atualizar os detalhes dos funcionarios.
    """
    return employee_service.update(data.dict())

@employee_router.delete("/employees/delete", response_model=str)
async def delete_employee(data: Dict[str, str], token: str = Depends(get_current_admin)):
    """
    Deletar um funcionario especifico.
    Apenas usuarios com nivel de acesso de gestor/gerente podem deletar funcionarios.
    """
    return employee_service.delete(data)

@employee_router.get("/employees/", response_model=List[Dict[str, str]])
async def get_all_employees(token: str = Depends(get_current_admin)):
    """
    Listar todos os funcionarios.
    Apenas usuarios com nivel de acesso de gestor/gerente podem visualizar a lista completa de funcionarios.
    """
    return employee_service.get_all()

