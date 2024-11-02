from pydantic import BaseModel
from utils.enums import GoalStatusEnum
from datetime import datetime

class GoalData(BaseModel):
    description: str
    start_date: datetime 
    # conclusion_date: datetime
    end_date: datetime
    status: GoalStatusEnum = GoalStatusEnum.not_started
    employee_id: int 

    def to_json(self):
        return {
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "status": self.status,
            "employee_id": self.employee_id
        }
class UpdateGoalData(BaseModel):
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
            "end_date": self.end_date,
            "employee_id": self.employee_id,
            "status": self.status,
            "conclusion_date": self.conclusion_date
        }