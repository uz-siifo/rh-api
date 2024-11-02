from fastapi import APIRouter, Depends, HTTPException, status
from middlewares.auth import authenticate_user, get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from _pydatetime import timedelta

router = APIRouter()

@router.post("/login", response_model=dict)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password) # funcao de autenticacao
    print(form_data.username, form_data.password)
    if isinstance(user, Exception):
        print("log: ", user)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credencias Invalidas",
        )
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES) # tempo de vida do token de acesso
    access_token = await create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )

    return {
        "token_de_acesso": access_token, 
        "tipo_de_token": "bearer",
        "name": user.get("name"),
        "email": user.get("email"),
        "username": user.get("username"),
        "user_id": user.get("id"),
        "role": user.get("role")
    }

@router.post("/logout")
async def logout(token: str = Depends(get_current_user)):
    return {"token": token}
    