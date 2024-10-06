from fastapi import APIRouter

routes = APIRouter()

@routes.get("/")
async def home():
    return {"hello, world"}