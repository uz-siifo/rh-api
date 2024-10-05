from .model import model as BaseModel

class PerformanceEvaluation(BaseModel):
    def __init__(self, employee_id, employee_rating_id, employee_goals_id, feedback, updated_at=None):
        super().__init__()
        self.employee_id = employee_id
        self.employee_rating_id = employee_rating_id
        self.employee_goals_id = employee_goals_id
        self.feedback = feedback
        self.updated_at = updated_at

    def to_json(self):
        return {
            "employee_id": self.employee_id,
            "employee_rating_id": self.employee_rating_id,
            "employee_goals_id": self.employee_goals_id,
            "feedback": self.feedback,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_json(cls, __performance_evaluation):
        try:
            return cls(
                employee_id=__performance_evaluation["employee_id"],
                employee_rating_id=__performance_evaluation["employee_rating_id"],
                employee_goals_id=__performance_evaluation["employee_goals_id"],
                feedback=__performance_evaluation["feedback"],
                updated_at=__performance_evaluation.get("updated_at")  # Usar get para evitar KeyError
            )
        except KeyError as e:
            print(e)
        except Exception as e:
            print(e)
