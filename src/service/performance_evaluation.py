from .service import Service
from sqlalchemy import select, update, delete, or_
from sqlalchemy.orm import Session
from model.models import PerformanceEvaluation

class PerformanceEvaluationService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        with Session(self.engine) as session:
            try:

                new_evaluation = PerformanceEvaluation.to_model(data)
                session.add(new_evaluation)
                session.commit()
                return new_evaluation.to_json()
            except Exception as e:
                session.rollback()
                return e

    def update(self, data):
        with Session(self.engine) as session:
            try: 

                performance_evaluation = session.query(PerformanceEvaluation).filter(PerformanceEvaluation.id == data.get("id")).first()
                for key, value in data.items():
                    if (hasattr(performance_evaluation, key)):
                        setattr(performance_evaluation, key, value) 
                session.commit()
                return performance_evaluation.to_json()
            except Exception as e:
                session.rollback()
                return e

    def delete(self, data):
        with Session(self.engine) as session:
            try:
                query = delete(PerformanceEvaluation).where(
                    PerformanceEvaluation.id == data.get('id')
                )
                session.execute(query)
                session.commit()
                return {"status": "OK"}
            
            except Exception as e:
                session.rollback()
                return e
        
    def get_all(self):
        with Session(self.engine) as session:
            from sqlalchemy import select, and_
            from model.models import EmployeeRating, Presences

            query = select(
                EmployeeRating.is_assiduous,
                EmployeeRating.is_collaborative,
                EmployeeRating.completed_goals,
                EmployeeRating.is_punctual,
                Presences.presences,
                Presences.absences,
                EmployeeRating.work_quality_rating,
                EmployeeRating.problem_solving_skills_rating,
                EmployeeRating.communication_skills_rating,
                EmployeeRating.time_management_skills_rating,
                EmployeeRating.leadership_skills_rating,
                EmployeeRating.employee_id

            ).where(
                and_(
                    PerformanceEvaluation.employee_id == EmployeeRating.employee_id,
                    PerformanceEvaluation.employee_id == Presences.employee_id
                )
            )

            result = session.execute(query).fetchall()
            performance_evaluations = []

            for row in result:
                performance_evaluation = row.tuple()
                performance_evaluations.append({
                    "is_assiduous": performance_evaluation[0],
                    "is_collaborative": performance_evaluation[1],
                    "completed_goals": performance_evaluation[2],
                    "is_punctual": performance_evaluation[3], 
                    "presences": performance_evaluation[4],
                    "absences": performance_evaluation[5],
                    "work_quality_rating": performance_evaluation[6],
                    "problem_solving_skills_rating": performance_evaluation[7],
                    "communication_skills_rating": performance_evaluation[8],
                    "time_management_skills_rating": performance_evaluation[9],
                    "leadership_skills_rating": performance_evaluation[10],
                    "employee_id": performance_evaluation[11]
                })

            return performance_evaluations


    def get_by_employee(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import select
            query = select(PerformanceEvaluation).where(PerformanceEvaluation.employee_id == data.get("employee_id"))
            result = session.execute(query).fetchall()
            return result