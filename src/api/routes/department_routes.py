from fastapi import APIRouter, Depends
from service.department import DepartmentService
from model.models import engine
from middlewares.auth import get_current_admin
from base_models.department import DepartmentData

department_router = APIRouter()
department_service = DepartmentService(engine)

@department_router.post("/admin/departments/create", response_model=dict)
async def create_department(data: DepartmentData, token: str = Depends(get_current_admin)):
    """
    Criar um novo departamento.
    Apenas usuarios com nivel de acesso de gestor/gerente podem criar novos departamentos.
    """
    result = department_service.create(data.to_json())
    if (isinstance(result, Exception)):
        return {"Error": str(result)} 
    return result

@department_router.delete("/admin/departments/delete", response_model=dict)
async def delete_department(data: dict, token: str = Depends(get_current_admin)):
    """
    Deletar um departamento especifico.
    Apenas usuarios com nivel de acesso de gestor/gerente podem deletar departamentos.
    """
    result = department_service.delete(data)
    if (isinstance(result, Exception)):
        return {"Error": str(result)} 
    return result

@department_router.put("/admin/departments/update", response_model=dict)
async def update_department(data: dict, token: str = Depends(get_current_admin)):
    """
    Atualizar informacoes de um departamento.
    Apenas usuarios com nivel de acesso de gestor/gerente podem atualizar departamentos.
    """
    result = department_service.update(data)
    if (isinstance(result, Exception)):
        return {"Error": str(result)} 
    return result

@department_router.get("/admin/departments/", response_model=list)
async def get_all_departments(token: str = Depends(get_current_admin)):
    """
    Listar todos os departamentos.
    Apenas usuarios com nivel de acesso de gestor/gerente podem visualizar a lista completa de departamentos.
    """
    return department_service.get_all()

@department_router.get("/admin/departments/by-employee", response_model=list)
async def get_all_departments_by_employee(data: dict, token: str = Depends(get_current_admin)):
    """
    Listar todos os departamentos associados a um empregado especifico.
    Apenas usuarios com nivel de acesso de gestor/gerente podem consultar esta informacao.
    """
    return department_service.get_all_by_employee(data)
