from .model import model as BaseModel

class Employee(BaseModel):
    def __init__(self, position_at_work, nuit, identity_card_bi, salary=0.0, date_admission=None, department_id=None, academic_level=None, updated_at=None) -> None:
        super().__init__()
        self.position_at_work = position_at_work
        self.nuit = nuit
        self.identity_card_bi = identity_card_bi
        self.salary = salary
        self.date_admission = date_admission
        self.department_id = department_id
        self.academic_level = academic_level
        self.updated_at = updated_at

    def to_json(self):
        return {
            "position_at_work": self.position_at_work,
            "nuit": self.nuit,
            "identity_card_bi": self.identity_card_bi,
            "salary": self.salary,
            "date_admission": self.date_admission,
            "department_id": self.department_id,
            "academic_level": self.academic_level,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_json(cls, employee_data):
        try:
            return cls(
                employee_data.get("position_at_work"),
                employee_data.get("nuit"),
                employee_data.get("identity_card_bi"),
                employee_data.get("salary", 0.0),
                employee_data.get("date_admission"),
                employee_data.get("department_id"),
                employee_data.get("academic_level"),
                employee_data.get("updated_at")
            )
        except Exception as e:
            print(f"Error: {e}")
