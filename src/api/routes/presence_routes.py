from fastapi import APIRouter, Depends, HTTPException, status
from service.presences import PresencesService
from model.models import engine
from middlewares.auth import get_current_admin, get_current_user
from api.base_models.models import PresenceData, UpdatePresenceData

# Inicializando o roteador e o servico
presences_router = APIRouter()
presences_service = PresencesService(engine)

# Rotas para gerenciamento de presencas

@presences_router.post("/admin/presences/create", response_model=dict)
async def create_presence(data: PresenceData, token: str = Depends(get_current_admin)):
    """
    Criar um novo registro de presenca.
    Apenas usuários com nivel de acesso de gestor/gerente podem criar registros de presenca.
    """
    result = presences_service.create(data.to_json())
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    
    return result

@presences_router.put("/admin/presences/update", response_model=dict)
async def update_presence(data: UpdatePresenceData, token: str = Depends(get_current_admin)):
    """
    Atualizar um registro de presenca existente.
    Apenas gestores/gerentes podem atualizar registros de presenca.
    """
    result = presences_service.update(data.to_json())
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@presences_router.delete("/admin/presences/delete", response_model=dict)
async def delete_presence(presence_id: int, token: str = Depends(get_current_admin)):
    """
    Deletar um registro de presenca especifico.
    Apenas gestores/gerentes podem deletar registros de presenca.
    """
    result = presences_service.delete({"id": presence_id})
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@presences_router.get("/admin/presences/", response_model=list)
async def get_all_presences(token: str = Depends(get_current_admin)):
    """
    Listar todos os registros de presenca.
    Apenas gestores/gerentes podem ver todos os registros de presenca.
    """
    presences = presences_service.get_all()
    # if isinstance(presences, str):
    #     raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=presences)
    return presences

@presences_router.get("/presences/employee/{employee_id}", response_model=list)
async def get_presences_by_employee(employee_id: int, token: str = Depends(get_current_user)):
    result = presences_service.get_by_employee({"employee_id": employee_id})
    return result
