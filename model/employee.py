from .model import model as BaseModel

class employee(BaseModel):
    def __init__(self, nuit, identity_card, salary, date_admission, academic_level, updated_at, department_name) -> None:
        self.nuit = nuit
        self.identity_card = identity_card
        self.salary = salary
        self.date_admission = date_admission
        self.academic_level = academic_level
        self.updated_at = updated_at
        self.departmente_name = department_name

    def to_json(self):
        return {
            "nuit": self.nuit,
            "identity_card": self.identity_card,
            "salary": self.salary,
            "academic_level": self.academic_level,
            "updated_at": self.updated_at,
            "department_name": self.departmente_name
        }
    
    def from_json(self, __employee):
        try:
            return employee(
                __employee["nuit"],
                __employee["identity_card"],
                __employee["salary"],
                __employee["date_admission"],
                __employee["academic_level"],
                __employee["updated_at"],
                __employee["department_name"]
            )
        except Exception as e:
              print(e)
