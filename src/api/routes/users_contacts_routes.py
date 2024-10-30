from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Optional
from api.base_models.models import ContactData, UpdateContactData
from service.contacts import ContactService
from model.models import engine
from middlewares.auth import get_current_user, get_current_admin

contact_router = APIRouter()
contact_service = ContactService(engine)

# Rotas para gerenciamento de contatos

@contact_router.post("/contacts/create", response_model=dict)
async def create_contact(data: ContactData, token: str = Depends(get_current_user)):
    """
    Criar um novo contato para o usuario.
    Apenas usuarios autenticados podem criar contatos.
    """
    result = contact_service.create(data.to_json())
    
    if result != {"status": "OK"}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))
    
    
    return result

@contact_router.delete("/contacts/delete", response_model=dict)
async def delete_contact(contact_id: int, contact: Optional[str] = None, token: str = Depends(get_current_user)):
    """
    Deletar um contato especifico.
    Apenas usuarios autenticados podem deletar seus contatos.
    """
    result = contact_service.delete({"id": contact_id, "contact": contact})
    
    if result != {"status": "OK"}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))

    return result

@contact_router.put("/contacts/update", response_model=dict)
async def update_contact(data: UpdateContactData, token: str = Depends(get_current_user)):
    """
    Atualizar um contato existente.
    Apenas usuarios autenticados podem atualizar seus contatos.
    """
    result = contact_service.update(data.to_json())

    if result != {"status": "OK"}:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(result))
    
    return result

@contact_router.get("/admin/contacts/", response_model=list)
async def get_all_contacts(token: str = Depends(get_current_admin)):
    """
    Listar todos os contatos do usuario autenticado.
    Apenas usuarios autenticados podem ver seus contatos.
    """
    contacts = contact_service.get_all()
    return contacts

@contact_router.get("/contacts/user/", response_model=list)
async def get_contacts_by_user(user_id: int, token: str = Depends(get_current_user)):
    """
    Listar todos os contatos de um usuario especifico.
    Apenas usuarios autenticados podem ver os contatos associados ao seu ID de usuario.
    """

    contacts = contact_service.get_all_by_user({"user_id": user_id})
    return contacts
