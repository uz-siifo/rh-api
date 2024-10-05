from .model import model as BaseModel

class Presence(BaseModel):
    def __init__(self, employee_id, month_records_id, updated_at=None) -> None:
        super().__init__()
        self.employee_id = employee_id
        self.month_records_id = month_records_id
        self.updated_at = updated_at

    def to_json(self):
        return {
            "employee_id": self.employee_id,
            "month_records_id": self.month_records_id,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_json(cls, presence_data):
        try:
            return cls(
                presence_data.get("employee_id"),
                presence_data.get("month_records_id"),
                presence_data.get("updated_at")
            )
        except Exception as e:
            print(f"Error: {e}")
