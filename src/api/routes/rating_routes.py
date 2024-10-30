from fastapi import APIRouter, Depends, HTTPException, status
from service.employee_rating import EmployeeRatingService
from model.models import engine
from middlewares.auth import get_current_admin, get_current_user
from api.base_models.models import RatingData, UpdateRatingData

rating_router = APIRouter()
rating_service = EmployeeRatingService(engine)

# Rotas acessiveis apenas a gestores/gerentes
@rating_router.post('/admin/ratings/create', response_model=dict)
async def create_rating(data: RatingData, token: str = Depends(get_current_admin)):
    """
    Criar uma nova avaliacao para um funcionario.
    Apenas usuarios com nivel de acesso de gestor/gerente podem criar avaliacoes.
    """
    result = rating_service.create(data.to_json())

    if isinstance(result, Exception):
        return {'Error': str(result)}
    
    return result

@rating_router.put('/admin/ratings/update', response_model=dict)
async def update_rating(data: UpdateRatingData, token: str = Depends(get_current_admin)):
    """
    Atualizar uma avaliacao existente.
    Apenas gestores/gerentes podem atualizar avaliacoes.
    """
    result = rating_service.update(data.to_json())
    if isinstance(result, Exception):
        return {'Error': str(result)}
    
    return rating_service.update(data.to_json())

@rating_router.delete('/admin/ratings/delete', response_model=dict)
async def delete_rating(rating_id: int, token: str = Depends(get_current_admin)):
    """
    Deletar uma avaliacao especifica.
    Apenas gestores/gerentes podem deletar avaliacoes.
    """

    result = rating_service.delete({"id": rating_id})
    if (isinstance(result, Exception)):
        return {"Error": str(result)}
    
    return rating_service.delete({"id": rating_id})

@rating_router.get("/admin/ratings/", response_model=list)
async def get_all_ratings(token: str = Depends(get_current_admin)):
    """
    Listar todas as avaliacoes de funcionarios.
    Apenas gestores/gerentes podem ver todas as avaliacoes.
    """
    return rating_service.get_all()

# Rotas acessiveis a todos os usuarios (normais ou gestores)
@rating_router.get("/ratings/{rating_id}", response_model=dict)
async def get_rating_by_id(rating_id: int, token: str = Depends(get_current_user)):
    """
    Obter uma avaliacao especifica pelo ID.
    Todos os usuarios autenticados podem visualizar uma avaliacao especifica.
    """
    rating = rating_service.get_by_id(rating_id)
    if (isinstance(rating, Exception)):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(rating))

    return rating

@rating_router.get("/ratings/employee/{employee_id}", response_model=dict)
async def get_ratings_by_employee_id(employee_id: int, token: str = Depends(get_current_user)):
    """
    Listar todas as avaliacoes de um funcionario especifico pelo ID.
    Todos os usuarios podem visualizar as suas proprias avaliacoes ou de outro funcionario.
    """
    return rating_service.get_by_employee_id(employee_id)
