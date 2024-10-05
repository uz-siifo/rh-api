from .model import model as BaseModel

class WorkingHours(BaseModel):
    def __init__(self, normal_hours=0, overtime=0, employee_id=None, updated_at=None) -> None:
        super().__init__()
        self.normal_hours = normal_hours
        self.overtime = overtime
        self.employee_id = employee_id
        self.updated_at = updated_at

    def to_json(self):
        return {
            "normal_hours": self.normal_hours,
            "overtime": self.overtime,
            "employee_id": self.employee_id,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_json(cls, working_hours_data):
        try:
            return cls(
                working_hours_data.get("normal_hours", 0),
                working_hours_data.get("overtime", 0),
                working_hours_data.get("employee_id"),
                working_hours_data.get("updated_at")
            )
        except Exception as e:
            print(f"Error: {e}")
