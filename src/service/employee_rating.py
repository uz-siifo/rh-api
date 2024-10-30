from .service import Service
from model.models import EmployeeRating
from sqlalchemy.orm import Session
from sqlalchemy import select

class EmployeeRatingService(Service):

    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        with Session(self.engine) as session:
            try:
                from .goals import GoalsService
                goals_service = GoalsService(self.engine)
                new_rating = EmployeeRating.to_model(data)
                new_rating.completed_goals = len(
                    goals_service.get_completed_goals_by_employee({
                        "employee_id": new_rating.employee_id
                    })
                )
                session.add(new_rating)
                session.commit()
                return new_rating.to_json()
            except Exception as e:
                session.rollback()
                return e

    def update(self, data):
        from sqlalchemy import update
        with Session(self.engine) as session:
            try:
                from .goals import GoalsService
                goals_service = GoalsService(self.engine)
                stmt = (
                    update(EmployeeRating)
                    .where(EmployeeRating.id == data.get('id'))
                    .values(
                        is_assiduous=data.get('is_assiduous', False),
                        is_collaborative=data.get('is_collaborative', False),
                        completed_goals= len(goals_service.get_completed_goals_by_employee({"employee_id": data.get("employee_id")})),
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
                return {"status": "OK"}
            
            except Exception as e:
                session.rollback()
                return e

    def delete(self, data):
        from sqlalchemy import delete
        with Session(self.engine) as session:
            try:
                query = delete(EmployeeRating).where(EmployeeRating.id == data.get('id'))
                session.execute(query)
                session.commit()
                return {"status": "OK"}
            
            except Exception as e:
                session.rollback()
                return e

    def get_all(self):
        try:
            with Session(self.engine) as session:
                query = select(EmployeeRating)
                result = session.execute(query).scalars().all()
                ratings = [rating.EmployeeRating.to_json() for rating in result]
                return ratings
        except Exception as e:
            return e

    def get_by_id(self, rating_id):
        try:
            with Session(self.engine) as session:
                from sqlalchemy import select
                query = select(EmployeeRating).where(EmployeeRating.id == rating_id)
                rating = session.execute(query).fetchone().tuple()[0]
                return rating.to_json()
            
        except Exception as e:
            return e

    def get_by_employee_id(self, employee_id):
        try:
            with Session(self.engine) as session:
                query = select(EmployeeRating).where(
                    EmployeeRating.employee_id == employee_id
                )
                result = session.execute(query).scalars().all()
                ratings = [rating.EmployeeRating.to_json() for rating in result]
                return ratings
        except Exception as e:
            return e
