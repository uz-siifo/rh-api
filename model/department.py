from .model import model as BaseModel

class department(BaseModel):
    def __init__(self, name, employee_nums, min_salary, max_salary, updated_at) -> None:
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
    
    def from_json(self, __department):
        try:
            return department(
                __department["name"],
                __department["employee_nums"],
                __department["min_salary"],
                __department["max_salary"],
                __department["updated_at"]
            )
        except Exception as e:
              print(e)