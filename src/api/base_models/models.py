from pydantic import BaseModel
from utils.enums import AccessLevelEnum, GoalStatusEnum

class UserData(BaseModel):
    id: int = None
    username: str = None
    passwd: str = None
    name: str = None
    nickname: str = None
    email: str = None
    contact: str = None
    access_level: AccessLevelEnum = AccessLevelEnum.user

    def to_json(self):
        return {
            "id": self.id,
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
    id: int = None
    user_id: int = None
    contact: str = None

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "contact": self.contact
        }
    
from datetime import datetime  
class EmployeeData(BaseModel):
    id: int = None
    name: str = None
    identity_card_bi: str = None
    nuit: str = None
    position: str = None
    department: str = None
    academic_level: str = None
    salary: float = None
    date_admission: datetime = None
    position_at_work: str = None

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
    nuit: str = None
    position: str = None
    department: str = None

    def to_json(self):
        return {
            "id": self.id,
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

class UserEmployeeData(BaseModel):
    user_id: int
    employee_id: int
    
    def to_json(self):
        return {
            "user_id": self.user_id,
            "employee_id": self.employee_id
        }

class UpdateUserEmployeeData(BaseModel):
    id: int
    user_id: int = None
    employee_id: int = None

    def to_json(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "employee_id": self.employee_id
        }
    

# Modelos para entrada de dados
class RatingData(BaseModel):
    employee_id: int = None
    is_assiduous: bool = None
    is_collaborative: bool = None
    is_punctual: bool = None
    work_quality_rating: int = None
    problem_solving_skills_rating: int = None
    communication_skills_rating: int = None
    time_management_skills_rating: int = None
    leadership_skills_rating: int = None

    def to_json(self):
        return {
            "employee_id": self.employee_id,
            "is_assiduous": self.is_assiduous,
            "is_collaborative": self.is_collaborative,
            "is_punctual": self.is_punctual,
            "work_quality_rating": self.work_quality_rating,
            "problem_solving_skills_rating": self.problem_solving_skills_rating,
            "communication_skills_rating": self.communication_skills_rating,
            "time_management_skills_rating": self.time_management_skills_rating,
            "leadership_skills_rating": self.leadership_skills_rating
        }

class UpdateRatingData(BaseModel):
    id: int
    employee_id: int = None
    is_assiduous: bool = None
    is_collaborative: bool = None
    is_punctual: bool = None
    work_quality_rating: int = None
    problem_solving_skills_rating: int = None
    communication_skills_rating: int = None
    time_management_skills_rating: int = None
    leadership_skills_rating: int = None

    def to_json(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "is_assiduous": self.is_assiduous,
            "is_collaborative": self.is_collaborative,
            "is_punctual": self.is_punctual,
            "work_quality_rating": self.work_quality_rating,
            "problem_solving_skills_rating": self.problem_solving_skills_rating,
            "communication_skills_rating": self.communication_skills_rating,
            "time_management_skills_rating": self.time_management_skills_rating,
            "leadership_skills_rating": self.leadership_skills_rating
        }
    

class PresenceData(BaseModel):
    employee_id: int
    month: int
    year: int
    presences: int
    absences: int

    def to_json(self):
        return {
            "employee_id": self.employee_id,
            "month": self.month,
            "year": self.year,
            "presences": self.presences,
            "absences": self.absences
        }

class UpdatePresenceData(BaseModel):
    id: int
    employee_id: int = None
    month: int = None
    year: int = None
    presences: int = None
    absences: int = None

    def to_json(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "month": self.month,
            "year": self.year,
            "presences": self.presences,
            "absences": self.absences
        }

# Modelos para entrada de dados
class PerformanceEvaluationData(BaseModel):
    employee_id: int
    employee_rating_id: int
    employee_goals_id: int
    feedback: str

    def to_json(self):
        return {
            "employee_id": self.employee_id,
            "employee_rating_id": self.employee_rating_id,
            "employee_goals_id": self.employee_goals_id
        }

class UpdatePerformanceEvaluationData(BaseModel):
    id: int
    employee_id: int = None
    employee_rating_id: int = None
    employee_goals_id: int = None
    feedback: str = None

    def to_json(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "employee_rating_id": self.employee_rating_id,
            "employee_goals_id": self.employee_goals_id,
            "feedback": self.feedback
        }
    
class GoalsData(BaseModel):
    description: str
    start_date: datetime 
    conclusion_date: datetime
    end_date: datetime
    status: GoalStatusEnum = GoalStatusEnum.not_started
    employee_id: int 

    def to_json(self):
        return {
            "description": self.description,
            "start_date": self.start_date,
            "conclusion_date": self.conclusion_date,
            "end_date": self.end_date,
            "status": self.status,
            "employee_id": self.employee_id
        }

class UpdateGoalsData(BaseModel):
    id: int
    description: str = None
    start_date: datetime = None 
    conclusion_date: datetime = None
    end_date: datetime = None
    status: GoalStatusEnum = GoalStatusEnum.not_started
    employee_id: int = None 

    def to_json(self):
        return {
            "id": self.id,
            "description": self.description,
            "start_date": self.start_date,
            "conclusion_date": self.conclusion_date,
            "end_date": self.end_date,
            "status": self.status,
            "employee_id": self.employee_id
        }