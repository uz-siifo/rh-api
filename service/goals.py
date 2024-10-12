from .service import Service
from sqlalchemy import select, update, delete, or_
from sqlalchemy.orm import Session
from model.models import Goals

class GoalsService(Service):
    def __init__(self, engine) -> None:
        super().__init__(engine)

    def create(self, data):
        try:
            with Session(self.engine) as session:
                new_goal = Goals.to_model(data)
                session.add(new_goal)
                session.commit()
                return "Goal created successfully"
        except Exception as e:
            return f"Error creating goal: {str(e)}"

    def update(self, data):
        try:
            with Session(self.engine) as session:
                stmt = (
                    update(Goals)
                    .where(Goals.id == data.get('id'))
                    .values(
                        description=data.get('description'),
                        start_date=data.get('start_date'),
                        conclusion_date=data.get('conclusion_date'),
                        end_date=data.get('end_date'),
                        employee_id=data.get('employee_id')
                    )
                )
                session.execute(stmt)
                session.commit()
                return "Goal updated successfully"
        except Exception as e:
            return f"Error updating goal: {str(e)}"

    def delete(self, data):
        try:
            with Session(self.engine) as session:
                query = delete(Goals).where(
                    or_(
                        Goals.id == data.get('id'),
                        Goals.description.like(f"%{data.get('description')}%")
                    )
                )
                session.execute(query)
                session.commit()
                return "Goal deleted successfully"
        except Exception as e:
            return f"Error deleting goal: {str(e)}"

    def get_all(self):
        try:
            with Session(self.engine) as session:
                query = select(Goals)
                result = session.execute(query).scalars().all()

                goals = [goal.to_json() for goal in result]
                return goals
        except Exception as e:
            return f"Error fetching goals: {str(e)}"
