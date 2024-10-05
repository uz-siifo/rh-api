from .model import model as BaseModel

class Department(BaseModel):
    def __init__(self, name, employee_nums=0, min_salary=0.0, max_salary=0.0, updated_at=None) -> None:
        super().__init__()
        self.name = name
        self.employee_nums = employee_nums
        self.min_salary = min_salary
        self.max_salary = max_salary
        self.updated_at = updated_at

    def to_json(self):
        return {
            "name": self.name,
            "employee_nums": self.employee_nums,
            "min_salary": self.min_salary,
            "max_salary": self.max_salary,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_json(cls, department_data):
        try:
            return cls(
                department_data.get("name"),
                department_data.get("employee_nums", 0),
                department_data.get("min_salary", 0.0),
                department_data.get("max_salary", 0.0),
                department_data.get("updated_at")
            )
        except Exception as e:
            print(f"Error: {e}")
