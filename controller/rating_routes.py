from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Optional
from pydantic import BaseModel
from service.employee_rating import EmployeeRatingService
from model.models import engine
from auth.auth_service import get_current_admin, get_current_user

rating_router = APIRouter()
rating_service = EmployeeRatingService(engine)

# Modelos para entrada de dados
class RatingData(BaseModel):
    employee_id: int
    is_assiduous: bool
    is_collaborative: bool
    is_punctual: bool
    work_quality_rating: int
    problem_solving_skills_rating: int
    communication_skills_rating: int
    time_management_skills_rating: int
    leadership_skills_rating: int

class UpdateRatingData(BaseModel):
    id: int
    employee_id: Optional[int] = None
    is_assiduous: Optional[bool] = None
    is_collaborative: Optional[bool] = None
    is_punctual: Optional[bool] = None
    work_quality_rating: Optional[int] = None
    problem_solving_skills_rating: Optional[int] = None
    communication_skills_rating: Optional[int] = None
    time_management_skills_rating: Optional[int] = None
    leadership_skills_rating: Optional[int] = None

# Rotas acessiveis apenas a gestores/gerentes
@rating_router.post("/ratings/create", response_model=str)
async def create_rating(data: RatingData, token: str = Depends(get_current_admin)):
    """
    Criar uma nova avaliacao para um funcionario.
    Apenas usuarios com nivel de acesso de gestor/gerente podem criar avaliacoes.
    """
    return rating_service.create(data.dict())

@rating_router.put("/ratings/update", response_model=str)
async def update_rating(data: UpdateRatingData, token: str = Depends(get_current_admin)):
    """
    Atualizar uma avaliacao existente.
    Apenas gestores/gerentes podem atualizar avaliacoes.
    """
    return rating_service.update(data.dict())

@rating_router.delete("/ratings/delete", response_model=str)
async def delete_rating(rating_id: int, token: str = Depends(get_current_admin)):
    """
    Deletar uma avaliacao especifica.
    Apenas gestores/gerentes podem deletar avaliacoes.
    """
    return rating_service.delete({"id": rating_id})

@rating_router.get("/ratings/", response_model=List[Dict[str, str]])
async def get_all_ratings(token: str = Depends(get_current_admin)):
    """
    Listar todas as avaliacoes de funcionarios.
    Apenas gestores/gerentes podem ver todas as avaliacoes.
    """
    return rating_service.get_all()

# Rotas acessiveis a todos os usuarios (normais ou gestores)
@rating_router.get("/ratings/{rating_id}", response_model=Dict[str, str])
async def get_rating_by_id(rating_id: int, token: str = Depends(get_current_user)):
    """
    Obter uma avaliacao especifica pelo ID.
    Todos os usuarios autenticados podem visualizar uma avaliacao especifica.
    """
    rating = rating_service.get_by_id(rating_id)
    if not rating:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avaliacao nao encontrada")
    return rating

@rating_router.get("/ratings/employee/{employee_id}", response_model=List[Dict[str, str]])
async def get_ratings_by_employee_id(employee_id: int, token: str = Depends(get_current_user)):
    """
    Listar todas as avaliacoes de um funcionario especifico pelo ID.
    Todos os usuarios podem visualizar as suas proprias avaliacoes ou de outro funcionario.
    """
    return rating_service.get_by_employee_id(employee_id)
