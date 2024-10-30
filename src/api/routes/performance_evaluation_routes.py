from fastapi import APIRouter, Depends, HTTPException, status
from service.performance_evaluation import PerformanceEvaluationService
from model.models import engine
from middlewares.auth import get_current_admin, get_current_user
from api.base_models.models import PerformanceEvaluationData, UpdatePerformanceEvaluationData

# Inicializando o roteador e o servico
performance_evaluation_router = APIRouter()
performance_evaluation_service = PerformanceEvaluationService(engine)

# Rotas para gerenciamento de avaliacoes de desempenho

@performance_evaluation_router.post("/admin/performance-evaluations/create", response_model=dict)
async def create_performance_evaluation(data: PerformanceEvaluationData, token: str = Depends(get_current_admin)):
    """
    Criar uma nova avaliacao de desempenho.
    Apenas usuarios com nivel de acesso de gestor/gerente podem criar avaliacoes.
    """
    result = performance_evaluation_service.create(data.to_json())
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))
    return result

@performance_evaluation_router.put("/admin/performance-evaluations/update", response_model=dict)
async def update_performance_evaluation(data: UpdatePerformanceEvaluationData, token: str = Depends(get_current_admin)):
    """
    Atualizar uma avaliacao de desempenho existente.
    Apenas gestores/gerentes podem atualizar avaliacoes.
    """
    result = performance_evaluation_service.update(data.to_json())
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))
    return result

@performance_evaluation_router.delete("/admin/performance-evaluations/delete", response_model=dict)
async def delete_performance_evaluation(evaluation_id: int, token: str = Depends(get_current_admin)):
    """
    Deletar uma avaliacao de desempenho especifica.
    Apenas gestores/gerentes podem deletar avaliacoes.
    """
    result = performance_evaluation_service.delete({"id": evaluation_id})
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))
    return result

@performance_evaluation_router.get("/admin/performance-evaluations/", response_model=list)
async def get_all_performance_evaluations(token: str = Depends(get_current_admin)):
    """
    Listar todas as avaliacoes de desempenho.
    Apenas gestores/gerentes podem ver todas as avaliacoes.
    """
    evaluations = performance_evaluation_service.get_all()
    return evaluations

@performance_evaluation_router.get("/performance-evaluations/employee/{employee_id}", response_model=list)
async def get_performance_evaluations_by_employee(employee_id: int, token: str = Depends(get_current_user)):
    """
    Listar todas as avaliacoes de desempenho de um funcionario especifico pelo ID.
    Todos os usuarios autenticados podem visualizar avaliacoes especificas.
    """
    evaluations = performance_evaluation_service.get_by_employee({"employee_id": employee_id})
    return evaluations
