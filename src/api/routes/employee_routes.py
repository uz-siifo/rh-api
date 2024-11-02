from service.employee import EmployeeService
from middlewares.auth import get_current_admin
from model.models import engine
from fastapi import APIRouter, Depends
from base_models.employee import Employee, UpdateEmployee

employee_router = APIRouter()
employee_service = EmployeeService(engine)

@employee_router.post("/admin/employees/create", response_model=dict)
async def create_employee(employee: Employee, token: str = Depends(get_current_admin)):
    """
    Criar um novo funcionario.
    Apenas usuarios com nivel de acesso de gestor/gerente podem criar novos funcionarios.
    """
    result = employee_service.create(employee.to_json())
    if (isinstance(result, Exception)):
        return {"Error": str(result)}

    return result

@employee_router.put("/admin/employees/update", response_model=dict)
async def update_employee(data: UpdateEmployee, token: str = Depends(get_current_admin)):
    """
    Atualizar informações de um funcionario.
    Apenas usuarios com nivel de acesso de gestor/gerente podem atualizar os detalhes dos funcionarios.
    """

    result = employee_service.update(data.to_json())

    if (isinstance(result, Exception)):
        return {"Error": str(result)}
    
    return employee_service.update(data.to_json())

@employee_router.delete("/admin/employees/delete", response_model=dict)
async def delete_employee(employee_id, token: str = Depends(get_current_admin)):
    """
    Deletar um funcionario especifico.
    Apenas usuarios com nivel de acesso de gestor/gerente podem deletar funcionarios.
    """
    result = employee_service.delete({"id": employee_id})
    if (isinstance(result, Exception)):
        return {"Error": str(result)}
    
    return result

@employee_router.get("/admin/employees/", response_model=list)
async def get_all_employees(token: str = Depends(get_current_admin)):
    """
    Listar todos os funcionarios.
    Apenas usuarios com nivel de acesso de gestor/gerente podem visualizar a lista completa de funcionarios.
    """
    return employee_service.get_all()

