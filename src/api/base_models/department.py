from pydantic import BaseModel

class DepartmentData(BaseModel):
    name: str
    
    def to_json(self):
        return {
            "name": self.name
        }
    
class UpdateDepartmentData(BaseModel):
    id: int
    name: str = None

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name
        }