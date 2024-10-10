from fastapi import FastAPI
from controller.routes import routes

app = FastAPI()

app.include_router(routes)

