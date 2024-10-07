from fastapi import FastAPI
from controller.routes import routes

app = FastAPI()

app.include_router(routes)
@app.get("/home")
def home() :
    return {"ola mundo"}


