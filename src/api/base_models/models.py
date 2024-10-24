from pydantic import BaseModel
from utils.enums import AccessLevelEnum

class UserData(BaseModel):
    username: str
    passwd: str
    name: str = None
    nickname: str = None
    email: str = None
    contact: str = None
    access_level: AccessLevelEnum = AccessLevelEnum.user

    def to_json(self):
        return {
            "name": self.name,
            "nickname": self.nickname,
            "email": self.email,
            "passwd": self.passwd,
            "contact": self.contact,
            "access_level": self.access_level,
            "username": self.username
        }
    
# Modelos para entrada de dados
class ContactData(BaseModel):
    user_id: int
    contact: str

    def to_json(self):
        return {
            "contact": self.contact,
            "user_id": self.user_id
        }

class UpdateContactData(BaseModel):
    id: int
    contact: str

    def to_json(self):
        return {
            "id": self.id,
            "contact": self.contact
        }
    
class EmployeeData(BaseModel):
    name: str
    identity_card_bi: str
    nuit: str
    position: str
    department: str

    def to_json(self):
        return {
            "name": self.name,
            "identity_card_bi": self.identity_card_bi,
            "nuit": self.nuit,
            "position": self.position,
            "department": self.department
        }

class UpdateEmployeeData(BaseModel):
    id: int
    name: str = None
    identity_card_bi: str = None
    nuit: str = None
    position: str = None
    department: str = None

    def to_json(self):
        return {
            "name": self.name,
            "identity_card_bi": self.identity_card_bi,
            "nuit": self.nuit,
            "position": self.position,
            "department": self.department
        }

class DepartmentData(BaseModel):
    name: str
    description: str = None
    min_salary: float
    max_salary: float
    employee_nums: int = None

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "min_salary": self.min_salary,
            "max_salary": self.max_salary
        }


from datetime import datetime  
class EmployeeData(BaseModel):
    name: str
    identity_card_bi: str
    nuit: str
    position: str
    department: str
    academic_level: str
    salary: float
    date_admission: datetime
    position_at_work: str

    def to_json(self):
        return {
            'id': self.id,
            'position_at_work': self.position_at_work,
            'nuit': self.nuit,
            'identity_card_bi': self.identity_card_bi,
            'salary': self.salary,
            'date_admission': self.date_admission,
            'academic_level': self.academic_level,
            'department_id': self.department
        }

class UpdateEmployeeData(BaseModel):
    id: int
    name: str = None
    identity_card_bi: str = None
    position: str = None
    department: str = None