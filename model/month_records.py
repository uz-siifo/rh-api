from .model import model as BaseModel

class MonthRecords(BaseModel):
    def __init__(self, month, year, presences=0, absences=0, updated_at=None) -> None:
        super().__init__()
        self.month = month
        self.year = year
        self.presences = presences
        self.absences = absences
        self.updated_at = updated_at

    def to_json(self):
        return {
            "month": self.month,
            "year": self.year,
            "presences": self.presences,
            "absences": self.absences,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_json(cls, month_record_data):
        try:
            return cls(
                month_record_data.get("month"),
                month_record_data.get("year"),
                month_record_data.get("presences", 0),
                month_record_data.get("absences", 0),
                month_record_data.get("updated_at")
            )
        except Exception as e:
            print(f"Error: {e}")
