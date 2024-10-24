from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Optional
from pydantic import BaseModel
from service.performance_evaluation import PerformanceEvaluationService
from model.models import engine
from auth.auth_service import get_current_admin, get_current_user

# Inicializando o roteador e o servico
performance_evaluation_router = APIRouter()
performance_evaluation_service = PerformanceEvaluationService(engine)

# Modelos para entrada de dados
class PerformanceEvaluationData(BaseModel):
    employee_id: int
    employee_rating_id: int
    employee_goals_id: int
    feedback: str

class UpdatePerformanceEvaluationData(BaseModel):
    id: int
    employee_id: Optional[int] = None
    employee_rating_id: Optional[int] = None
    employee_goals_id: Optional[int] = None
    feedback: Optional[str] = None

# Rotas para gerenciamento de avaliacoes de desempenho

@performance_evaluation_router.post("/performance-evaluations/create", response_model=str)
async def create_performance_evaluation(data: PerformanceEvaluationData, token: str = Depends(get_current_admin)):
    """
    Criar uma nova avaliacao de desempenho.
    Apenas usuarios com nivel de acesso de gestor/gerente podem criar avaliacoes.
    """
    result = performance_evaluation_service.create(data.dict())
    if "Error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@performance_evaluation_router.put("/performance-evaluations/update", response_model=str)
async def update_performance_evaluation(data: UpdatePerformanceEvaluationData, token: str = Depends(get_current_admin)):
    """
    Atualizar uma avaliacao de desempenho existente.
    Apenas gestores/gerentes podem atualizar avaliacoes.
    """
    result = performance_evaluation_service.update(data.dict())
    if "Error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@performance_evaluation_router.delete("/performance-evaluations/delete", response_model=str)
async def delete_performance_evaluation(evaluation_id: int, token: str = Depends(get_current_admin)):
    """
    Deletar uma avaliacao de desempenho especifica.
    Apenas gestores/gerentes podem deletar avaliacoes.
    """
    result = performance_evaluation_service.delete({"id": evaluation_id})
    if "Error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@performance_evaluation_router.get("/performance-evaluations/", response_model=List[Dict[str, str]])
async def get_all_performance_evaluations(token: str = Depends(get_current_admin)):
    """
    Listar todas as avaliacoes de desempenho.
    Apenas gestores/gerentes podem ver todas as avaliacoes.
    """
    evaluations = performance_evaluation_service.get_all()
    if isinstance(evaluations, str) and "Error" in evaluations:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=evaluations)
    return evaluations

@performance_evaluation_router.get("/performance-evaluations/employee/{employee_id}", response_model=List[Dict[str, str]])
async def get_performance_evaluations_by_employee(employee_id: int, token: str = Depends(get_current_user)):
    """
    Listar todas as avaliacoes de desempenho de um funcionario especifico pelo ID.
    Todos os usuarios autenticados podem visualizar avaliacoes especificas.
    """
    evaluations = performance_evaluation_service.get_by_employee({"employee_id": employee_id})
    if isinstance(evaluations, str) and "Error" in evaluations:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=evaluations)
    return evaluations
