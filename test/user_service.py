from src.service.user import UserService
from model.models import engine

user_service = UserService(engine)

print(user_service.create({
    ""
}))