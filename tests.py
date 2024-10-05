# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"Message": "Hello, world"}

# @app.get("/home/{name}")
# def init(name: str):
#     return {"name": name}

# from db.connect import cur
from service.user import user_service
user = user_service()

user.create()
# cur.execute("select* from department;")
