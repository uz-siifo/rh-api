from .model import model as BaseModel

class UserEmployee(BaseModel):
    def __init__(self, user_id, employee_id, updated_at=None) -> None:
        super().__init__()
        self.user_id = user_id
        self.employee_id = employee_id
        self.updated_at = updated_at

    def to_json(self):
        return {
            "user_id": self.user_id,
            "employee_id": self.employee_id,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_json(cls, __user_employee):
        try:
            return cls(
                __user_employee["user_id"],
                __user_employee["employee_id"],
                __user_employee.get("updated_at")  # Usa get para evitar KeyError
            )
        except KeyError as e:
            print(e)
        except Exception as e:
            print(e)
