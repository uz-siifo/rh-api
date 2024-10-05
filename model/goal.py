from .model import model as BaseModel

class goal(BaseModel):
    def __init__(self, description, start_date, end_date, conclusion_date, updated_at, employee_id)->None:
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.conclusion_date = conclusion_date
        self.updated_at = updated_at
        self.employee_id = employee_id
    
    def to_json(self):
        return {
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "updated_at": self.updated_at,
            "conclusion_date": self.conclusion_date,
            "employee_id": self.employee_id
        }
    
    def from_json(self, __goal):
        try:
            return goal(
                __goal["description"],
                __goal["start_date"],
                __goal["end_date"],
                __goal["conclusion_date"],
                __goal["updated_at"],
                __goal["employee_id"]
            )

        except Exception as error:
            print(error)
