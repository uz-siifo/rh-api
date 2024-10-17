from .service import Service
from sqlalchemy import select, update, delete, or_
from sqlalchemy.orm import Session
from model.models import PerformanceEvaluation

class PerformanceEvaluationService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_evaluation = PerformanceEvaluation.to_model(data)
                session.add(new_evaluation)
                session.commit()
                return "Performance evaluation created successfully"
        except Exception as e:
            return f"Error creating performance evaluation: {str(e)}"

    def update(self, data):
        try:
            with Session(self.engine) as session:
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
                return "Performance evaluation updated successfully"
        except Exception as e:
            return f"Error updating performance evaluation: {str(e)}"

    def delete(self, data):
        try:
            with Session(self.engine) as session:
                query = delete(PerformanceEvaluation).where(
                    PerformanceEvaluation.id == data.get('id')
                )
                session.execute(query)
                session.commit()
                return "Performance evaluation deleted successfully"
        except Exception as e:
            return f"Error deleting performance evaluation: {str(e)}"

    def get_all(self):
        try:
            with Session(self.engine) as session:
                query = select(PerformanceEvaluation)
                result = session.execute(query).scalars().all()

                evaluations = [evaluation.to_json() for evaluation in result]
                return evaluations
        except Exception as e:
            return f"Error fetching performance evaluations: {str(e)}"
        
    def get_by_employee(self, data):
        try:
            with Session(self.engine) as session:
                from sqlalchemy import select
                query = select(PerformanceEvaluation).where(PerformanceEvaluation.employee_id == data.get("employee_id"))
                result = session.execute(query).fetchall()
                return result

        except Exception as e:
            return f"Error fetching performance evaluations: {str(e)}"

