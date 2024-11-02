from pydantic import BaseModel

class RatingData(BaseModel):
    is_assiduous: bool
    is_collaborative: bool
    is_punctual: bool
    work_quality_rating: float
    problem_solving_skills_rating: float
    communication_skills_rating: float
    time_management_skills_rating: float
    leadership_skills_rating: float
    employee_id: int

    def to_json(self):
        return {
            "is_assiduous": self.is_assiduous,
            "is_collaborative": self.is_collaborative,
            "is_punctual": self.is_punctual,
            "work_quality_rating": self.work_quality_rating,
            "problem_solving_skills_rating": self.problem_solving_skills_rating,
            "communication_skills_rating": self.communication_skills_rating,
            "time_management_skills_rating": self.time_management_skills_rating,
            "leadership_skills_rating": self.leadership_skills_rating,
            "employee_id": self.employee_id
        }

class UpdateRatingData(BaseModel):
    id: int
    is_assiduous: bool = None
    is_collaborative: bool = None
    is_punctual: bool = None
    work_quality_rating: float = None 
    problem_solving_skills_rating: float = None
    communication_skills_rating: float = None
    time_management_skills_rating: float = None
    leadership_skills_rating: float = None
    employee_id: int

    def to_json(self):
        return {
            "id": self.id,
            "is_assiduous": self.is_assiduous,
            "is_collaborative": self.is_collaborative,
            "is_punctual": self.is_punctual,
            "work_quality_rating": self.work_quality_rating,
            "problem_solving_skills_rating": self.problem_solving_skills_rating,
            "communication_skills_rating": self.communication_skills_rating,
            "time_management_skills_rating": self.time_management_skills_rating,
            "leadership_skills_rating": self.leadership_skills_rating,
            "employee_id": self.employee_id
        }
