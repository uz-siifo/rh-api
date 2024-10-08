from fastapi import APIRouter
from model.model import engine
from service.user import UserService
from fastapi import Request

routes = APIRouter()

@routes.post("/create/user/")
async def create_user(request: Request):
    user = await request.json()
    
    service = UserService(engine)
    result = service.create(user)
    return {"status": result}

@routes.get("/get/users/")
async def read_all_users():
    service = UserService(engine)
    users = service.get_all()
    return users
