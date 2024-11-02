from pydantic import BaseModel
from utils.enums import Role, EmployeeState
from datetime import datetime

class Employee(BaseModel):
    username: str
    passwd: str
    name: str
    nickname: str
    email: str
    contact: str
    role: Role = Role.user
    state: EmployeeState = EmployeeState.inactive
    position: str
    department: str
    academic_level: str
    date_admission: datetime

    def to_json(self):
        return {
            "username": self.username,
            "passwd": self.passwd,
            "name": self.name,
            "nickname": self.nickname,
            "email": self.email,
            "contact": self.contact,
            "role": self.role,
            "state": self.state,
            "position": self.position,
            "department": self.department,
            "academic_level": self.academic_level,
            "date_admission": self.date_admission
        }

class UpdateEmployee(BaseModel):
    id:int
    username: str = None
    passwd: str = None
    name: str = None
    nickname: str = None
    email: str = None
    contact: str = None
    role: Role = Role.user
    state: EmployeeState = EmployeeState.inactive
    position: str = None
    department: str = None
    academic_level: str = None
    date_admission: datetime = None

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "passwd": self.passwd,
            "name": self.name,
            "nickname": self.nickname,
            "email": self.email,
            "contact": self.contact,
            "role": self.role,
            "state": self.state,
            "position": self.position,
            "department": self.department,
            "academic_level": self.academic_level,
            "date_admission": self.date_admission
        }

