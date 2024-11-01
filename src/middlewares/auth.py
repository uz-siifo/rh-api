from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from model.models import engine
from service.user import UserService
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import List
import jwt
from datetime import datetime, timedelta

import os
SECRET_KEY = os.getenv("SECRET_KEY", "")  # Obtendo a chave secreta do ambiente ou usando uma padrao
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

ALGORITHM = "HS256"  # Algoritmo usado para codificacao JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Tempo de expiracao do token

security = HTTPBasic()

# Funcao para autenticar um usuario com base em username e senha
async def authenticate_user(username: str, password: str):
    try:
        user_service = UserService(engine)
        user = user_service.is_user({"username": username, "passwd": password})
        
        return {
            "name": user.get("name"),
            "email": user.get("email"),
            "username": user.get("username"),
            "user_id": user.get("id"),
            "role": user.get("access_level")
        }
    
    except Exception as e:
        return e

# Funcao para criar um token de acesso JWT
async def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta  # Define o tempo de expiracao do token
    else:
        expire = datetime.now() + timedelta(minutes=15)  # Tempo padrao de expiracao
    to_encode.update({"exp": expire})  # Adiciona a data de expiracao ao payload do token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  # Codifica o token JWT
    return encoded_jwt

# Funcao para obter o usuario atual com base no token JWT
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # Decodifica o token JWT
        username: str = payload.get("sub")  # Extrai o username do payload
        if username is None: 
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return username
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)  # Lanca excecao se o token for invalido

# Funcao para verificar se o usuario atual e admin
async def get_current_admin(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])  # Decodifica o token JWT
        username: str = payload.get("sub")  # Extrai o username do payload
        
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError as e:
        print(f"Erro ao decodificar o token JWT: {e}")  # Loga o erro de decodificacao
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)  # Lanca excecao se o token for invalido

    # Verifica se o usuario e admin usando o servico de usuario
    from service.user import UserService
    user_service = UserService(engine)

    if not user_service.is_admin(username):  # Se o usuario nao for admin, lanca uma excecao HTTP 403
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Somente Admins e que têm acesso a este servico",
        )
    return username