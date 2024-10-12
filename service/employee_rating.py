from .service import Service
from model.models import EmployeeRating
from sqlalchemy.orm import Session
from sqlalchemy import select

class EmployeeRatingService(Service):

    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_rating = EmployeeRating.to_model(data)
                session.add(new_rating)
                session.commit()
                return "Rating created successfully"
        except Exception as e:
            return f"Error creating rating: {str(e)}"

    def update(self, data):
        from sqlalchemy import update
        try:
            with Session(self.engine) as session:
                stmt = (
                    update(EmployeeRating)
                    .where(EmployeeRating.id == data.get('id'))
                    .values(
                        is_assiduous=data.get('is_assiduous', False),
                        is_collaborative=data.get('is_collaborative', False),
                        completed_goals=data.get('completed_goals', 0),
                        is_punctual=data.get('is_punctual', False),
                        work_quality_rating=data.get('work_quality_rating', 0),
                        problem_solving_skills_rating=data.get('problem_solving_skills_rating', 0),
                        communication_skills_rating=data.get('communication_skills_rating', 0),
                        time_management_skills_rating=data.get('time_management_skills_rating', 0),
                        leadership_skills_rating=data.get('leadership_skills_rating', 0)
                    )
                )
                session.execute(stmt)
                session.commit()
                return "Rating updated successfully"
        except Exception as e:
            return f"Error updating rating: {str(e)}"

    def delete(self, data):
        from sqlalchemy import delete
        try:
            with Session(self.engine) as session:
                query = delete(EmployeeRating).where(EmployeeRating.id == data.get('id'))
                session.execute(query)
                session.commit()
                return "Rating deleted successfully"
        except Exception as e:
            return f"Error deleting rating: {str(e)}"

    def get_all(self):
        try:
            with Session(self.engine) as session:
                query = select(EmployeeRating)
                result = session.execute(query).fetchall()
                ratings = [row.EmployeeRating.to_json() for row in result]
                return ratings
        except Exception as e:
            return f"Erro ao buscar avalicoes: {str(e)}"

    def get_by_id(self, rating_id):
        try:
            with Session(self.engine) as session:
                rating = session.scalar(select(EmployeeRating).where(EmployeeRating.id == rating_id))
                return rating.to_json() if rating else None
        except Exception as e:
            return f"Erro ao buscar a avalicao pelo id: {str(e)}"

    def get_by_employee_id(self, employee_id):
        try:
            with Session(self.engine) as session:
                ratings = session.execute(select(EmployeeRating).where(EmployeeRating.employee_id == employee_id)).fetchall()
                return [row.EmployeeRating.to_json() for row in ratings]
        except Exception as e:
            return f"Erro ao buscar a avalicao pelo employee_id: {str(e)}"
