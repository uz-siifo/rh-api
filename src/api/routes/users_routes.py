from auth.auth_service import *
from service.user import UserService
from model.models import engine
from fastapi import APIRouter

users_routes = APIRouter()
user_service = UserService(engine)

"""
    rota para o login dos usuarios, esta rota nao tem nenhuma dependecia
"""
@users_routes.post("/login", response_model=dict)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password) # funcao de autenticacao
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credencias Invalidas",
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # tempo de vida do token de acesso
    access_token = await create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"token_de_acesso": access_token, "tipo_de_token": "bearer"}

"""
    rota para criacao de novos usuarios, esta rota e restrita apenas o admin do sistema
    Tem uma dependecia!
"""

from api.base_models.models import UserData
@users_routes.post("/users/create", response_model=str)
async def create_user(data: UserData, token: str = Depends(get_current_admin)):
    return user_service.create(data.to_json())

"""
    rota para atualizar inforcamacoes dos usuarios, esta rota e restrita apenas o admin do sistema
    Tem uma dependecia! 
"""
@users_routes.put("/users/update", response_model=str)
async def update_user(data: UserData, token: str = Depends(get_current_admin)):
    return user_service.update(data.to_json())

@users_routes.delete("/users/delete", response_model=str)
async def delete_user(data: dict, token: str = Depends(get_current_admin)):
    return user_service.delete(data)

@users_routes.get("/users/", response_model=List[dict])
async def get_all_users(token: str = Depends(get_current_admin)):
    return user_service.get_all()

@users_routes.get("/users/{user_id}", response_model=dict)
async def get_user_by_id(user_id: int, token: str = Depends(get_current_user)):
    return user_service.get_by_id({"id": user_id})

@users_routes.get("/users/by-name/{name}", response_model=dict)
async def get_user_by_name(name: str, token: str = Depends(get_current_user)):
    return user_service.get_by_name({"name": name})
