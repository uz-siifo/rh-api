from .model import model as BaseModel

class Goal(BaseModel):
    def __init__(self, description, start_date, conclusion_date, end_date, employee_id, updated_at=None) -> None:
        super().__init__()
        self.description = description
        self.start_date = start_date
        self.conclusion_date = conclusion_date
        self.end_date = end_date
        self.employee_id = employee_id
        self.updated_at = updated_at

    def to_json(self):
        return {
            "description": self.description,
            "start_date": self.start_date,
            "conclusion_date": self.conclusion_date,
            "end_date": self.end_date,
            "employee_id": self.employee_id,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_json(cls, goal_data):
        try:
            return cls(
                goal_data.get("description"),
                goal_data.get("start_date"),
                goal_data.get("conclusion_date"),
                goal_data.get("end_date"),
                goal_data.get("employee_id"),
                goal_data.get("updated_at")
            )
        except Exception as e:
            print(f"Error: {e}")
