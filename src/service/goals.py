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
                return new_goal.to_json()
            
        except Exception as e:
            return f"Error creating goal: {str(e)}"

    def update(self, data):
            with Session(self.engine) as session:
                try:
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
                    session.rollback()
                    return f"Error updating goal: {str(e)}"

    def delete(self, data):
        with Session(self.engine) as session:
            try:
                query = delete(Goals).where(
                    or_(
                        Goals.id == data.get('id')
                    )
                )
                session.execute(query)
                session.commit()
                return "Goal deleted successfully"
            except Exception as e:
                session.rollback()
                return f"Error deleting goal: {str(e)}"

    def get_all(self):
        with Session(self.engine) as session:
            query = select(Goals)
            result = session.execute(query).scalars().all()

            goals = [goal.to_json() for goal in result]
            return goals
    
    def get_completed_goals_by_employee(self, data):
        with Session(self.engine) as session:
            from sqlalchemy import select, and_
            from utils.enums import GoalStatusEnum
            query = select(Goals).where(
                and_(
                    Goals.employee_id == data.get("employee_id"),
                    Goals.status == GoalStatusEnum.completed
                )
            )
            result = session.execute(query).scalars().all()
            goals = [goal.to_json() for goal in result]
            return goals