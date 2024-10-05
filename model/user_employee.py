from .model import model as BaseModel

class user_employee(BaseModel):
    def __init__(self, user_id, employee_id, updated_at) -> None:
        self.user_id = user_id
        self.employee_id = employee_id
        self.updated_at = updated_at

    def to_json(self):
        return {
            "user_id": self.user_id,
            "employee_id": self.employee_id,
            "updated_id": self.updated_at 
        }
    
    def from_json(self, __user_employee):
        try:
            return user_employee(
                __user_employee["user_id"],
                __user_employee["employee_id"],
                __user_employee["updated_at"]
            )
        except Exception as e:
            print(e)