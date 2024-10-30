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
                stmt = (
                    update(PerformanceEvaluation)
                    .where(PerformanceEvaluation.id == data.get('id'))
                    .values(
                        employee_id=data.get('employee_id'),
                        employee_rating_id=data.get('employee_rating_id'),
                        employee_goals_id=data.get('employee_goals_id'),
                        feedback=data.get('feedback')
                    )
                )
                session.execute(stmt)
                session.commit()
                return {"status": "OK"}
            
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
            query = select(PerformanceEvaluation)
            result = session.execute(query).scalars().all()

            evaluations = [evaluation.to_json() for evaluation in result]
            return evaluations
        
    def get_by_employee(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import select
            query = select(PerformanceEvaluation).where(PerformanceEvaluation.employee_id == data.get("employee_id"))
            result = session.execute(query).fetchall()
            return result
