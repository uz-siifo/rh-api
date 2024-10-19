from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Optional
from pydantic import BaseModel
from service.presences import PresencesService
from model.models import engine
from auth.auth_service import get_current_admin, get_current_user

# Inicializando o roteador e o servico
presences_router = APIRouter()
presences_service = PresencesService(engine)

# Modelos para entrada de dados
class PresenceData(BaseModel):
    employee_id: int
    month_records_id: int

class UpdatePresenceData(BaseModel):
    id: int
    employee_id: Optional[int] = None
    month_records_id: Optional[int] = None

# Rotas para gerenciamento de presencas

@presences_router.post("/presences/create", response_model=str)
async def create_presence(data: PresenceData, token: str = Depends(get_current_admin)):
    """
    Criar um novo registro de presenca.
    Apenas usuários com nivel de acesso de gestor/gerente podem criar registros de presenca.
    """
    result = presences_service.create(data.dict())
    if "Error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@presences_router.put("/presences/update", response_model=str)
async def update_presence(data: UpdatePresenceData, token: str = Depends(get_current_admin)):
    """
    Atualizar um registro de presenca existente.
    Apenas gestores/gerentes podem atualizar registros de presenca.
    """
    result = presences_service.update(data.dict())
    if "Error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@presences_router.delete("/presences/delete", response_model=str)
async def delete_presence(presence_id: int, token: str = Depends(get_current_admin)):
    """
    Deletar um registro de presenca especifico.
    Apenas gestores/gerentes podem deletar registros de presenca.
    """
    result = presences_service.delete({"id": presence_id})
    if "Error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@presences_router.get("/presences/", response_model=List[Dict[str, str]])
async def get_all_presences(token: str = Depends(get_current_admin)):
    """
    Listar todos os registros de presenca.
    Apenas gestores/gerentes podem ver todos os registros de presenca.
    """
    presences = presences_service.get_all()
    if isinstance(presences, str) and "Error" in presences:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=presences)
    return presences
