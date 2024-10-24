from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Optional
from pydantic import BaseModel
from service.month_records import MonthRecordsService
from model.models import engine
from auth.auth_service import get_current_admin, get_current_user

# Inicializando o roteador e o servico
month_records_router = APIRouter()
month_records_service = MonthRecordsService(engine)

# Modelos para entrada de dados
class MonthRecordData(BaseModel):
    month: str
    year: int
    presences: int
    absences: int

class UpdateMonthRecordData(BaseModel):
    id: int
    month: Optional[str] = None
    year: Optional[int] = None
    presences: Optional[int] = None
    absences: Optional[int] = None

# Rotas para gerenciamento de registros de meses

@month_records_router.post("/month-records/create", response_model=str)
async def create_month_record(data: MonthRecordData, token: str = Depends(get_current_admin)):
    """
    Criar um novo registro de mes.
    Apenas usuarios com nivel de acesso de gestor/gerente podem criar registros.
    """
    result = month_records_service.create(data.dict())
    if "Error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@month_records_router.put("/month-records/update", response_model=str)
async def update_month_record(data: UpdateMonthRecordData, token: str = Depends(get_current_admin)):
    """
    Atualizar um registro de mes existente.
    Apenas gestores/gerentes podem atualizar registros.
    """
    result = month_records_service.update(data.dict())
    if "Error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@month_records_router.delete("/month-records/delete", response_model=str)
async def delete_month_record(record_id: int, token: str = Depends(get_current_admin)):
    """
    Deletar um registro de mes especifico.
    Apenas gestores/gerentes podem deletar registros.
    """
    result = month_records_service.delete({"id": record_id})
    if "Error" in result:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=result)
    return result

@month_records_router.get("/month-records/", response_model=List[Dict[str, str]])
async def get_all_month_records(token: str = Depends(get_current_admin)):
    """
    Listar todos os registros de meses.
    Apenas gestores/gerentes podem ver todos os registros.
    """
    records = month_records_service.get_all()
    if isinstance(records, str) and "Error" in records:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=records)
    return records

@month_records_router.get("/month-records/{record_id}", response_model=Dict[str, str])
async def get_month_record_by_id(record_id: int, token: str = Depends(get_current_user)):
    """
    Obter um registro de mes especifico pelo ID.
    Todos os usuarios autenticados podem visualizar um registro especifico.
    """
    record = month_records_service.get_by_id(record_id)
    if not record:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Registro de mes não encontrado")
    return record

@month_records_router.get("/month-records/year/{year}/month/{month}", response_model=List[Dict[str, str]])
async def get_month_records_by_year_and_month(year: int, month: str, token: str = Depends(get_current_user)):
    """
    Listar registros de meses especificos por ano e mes.
    Todos os usuarios autenticados podem visualizar registros especificos.
    """
    records = month_records_service.get_by_year_and_month(year, month)
    if isinstance(records, str) and "Error" in records:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=records)
    return records
