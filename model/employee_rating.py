from .model import model as BaseModel

class EmployeeRating(BaseModel):
    def __init__(self, is_assiduous, is_collaborative, completed_goals, 
                 is_punctual, work_quality_rating, problem_solving_skills_rating, 
                 communication_skills_rating, time_management_skills_rating, 
                 leadership_skills_rating, employee_id, created_at=None, updated_at=None) -> None:
        super().__init__()
        self.is_assiduous = is_assiduous
        self.is_collaborative = is_collaborative
        self.completed_goals = completed_goals
        self.is_punctual = is_punctual
        self.work_quality_rating = work_quality_rating
        self.problem_solving_skills_rating = problem_solving_skills_rating
        self.communication_skills_rating = communication_skills_rating
        self.time_management_skills_rating = time_management_skills_rating
        self.leadership_skills_rating = leadership_skills_rating
        self.employee_id = employee_id
        self.created_at = created_at
        self.updated_at = updated_at

    def to_json(self):
        return {
            "is_assiduous": self.is_assiduous,
            "is_collaborative": self.is_collaborative,
            "completed_goals": self.completed_goals,
            "is_punctual": self.is_punctual,
            "work_quality_rating": self.work_quality_rating,
            "problem_solving_skills_rating": self.problem_solving_skills_rating,
            "communication_skills_rating": self.communication_skills_rating,
            "time_management_skills_rating": self.time_management_skills_rating,
            "leadership_skills_rating": self.leadership_skills_rating,
            "employee_id": self.employee_id,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_json(cls, data):
        try:
            return cls(
                is_assiduous=data["is_assiduous"],
                is_collaborative=data["is_collaborative"],
                completed_goals=data["completed_goals"],
                is_punctual=data["is_punctual"],
                work_quality_rating=data["work_quality_rating"],
                problem_solving_skills_rating=data["problem_solving_skills_rating"],
                communication_skills_rating=data["communication_skills_rating"],
                time_management_skills_rating=data["time_management_skills_rating"],
                leadership_skills_rating=data["leadership_skills_rating"],
                employee_id=data["employee_id"],
                created_at=data.get("created_at"), 
                updated_at=data.get("updated_at")
            )
        except KeyError as e:
            print(f"Missing key: {e}")
        except Exception as e:
            print(e)
