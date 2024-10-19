from fastapi import APIRouter, Depends
from typing import List
from service.department import DepartmentService
from model.models import engine
from auth.auth_service import get_current_admin  # Funcao para verificar se o usuario é um gestor/gerente
from base_models.models import DepartmentData

# Definicao da API Router
department_router = APIRouter()
department_service = DepartmentService(engine)

@department_router.post("/departments/create", response_model=str)
async def create_department(data: DepartmentData, token: str = Depends(get_current_admin)):
    """
    Criar um novo departamento.
    Apenas usuarios com nivel de acesso de gestor/gerente podem criar novos departamentos.
    """
    return department_service.create(data.to_json())

@department_router.delete("/departments/delete", response_model=str)
async def delete_department(data: dict, token: str = Depends(get_current_admin)):
    """
    Deletar um departamento especifico.
    Apenas usuarios com nivel de acesso de gestor/gerente podem deletar departamentos.
    """
    return department_service.delete(data)

@department_router.put("/departments/update", response_model=str)
async def update_department(data: dict, token: str = Depends(get_current_admin)):
    """
    Atualizar informacoes de um departamento.
    Apenas usuarios com nivel de acesso de gestor/gerente podem atualizar departamentos.
    """
    return department_service.update(data)

@department_router.get("/departments/", response_model=List[dict])
async def get_all_departments(token: str = Depends(get_current_admin)):
    """
    Listar todos os departamentos.
    Apenas usuarios com nivel de acesso de gestor/gerente podem visualizar a lista completa de departamentos.
    """
    return department_service.get_all()

@department_router.get("/departments/by-employee", response_model=List[dict])
async def get_all_departments_by_employee(data: dict, token: str = Depends(get_current_admin)):
    """
    Listar todos os departamentos associados a um empregado especifico.
    Apenas usuarios com nivel de acesso de gestor/gerente podem consultar esta informacao.
    """
    return department_service.get_all_by_employee(data)
