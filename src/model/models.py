from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from settings import Settings
from sqlalchemy.types import Enum as PgEnum
from utils.enums import *
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from sqlalchemy import (
    Column, ForeignKey, Text, Float, BigInteger, Boolean, Integer, String, DateTime, func 
)

engine = create_engine(Settings().DATABASE_URL)
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True) # os dados ficam armazendos na memoria

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    nickname = Column(String(255), nullable=False)
    username = Column(String(225), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    passwd = Column(String(255), nullable=False)
    access_level = Column(PgEnum(AccessLevelEnum, name="access_level_enum"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    contacts = relationship("UserContact", back_populates="user", cascade="all, delete", passive_deletes=True) 
    employees = relationship("Employee", secondary="user_employee", back_populates="users") 

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            nickname=data.get('nickname'),
            username=data.get('username'),
            email=data.get('email'),
            passwd=data.get('passwd'),
            access_level=data.get('access_level')
        )

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'nickname': self.nickname,
            'username': self.username,
            'email': self.email,
            'passwd': self.passwd,
            'access_level': self.access_level.name if self.access_level else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'contacts': [contact.to_json() for contact in self.contacts]
        }

class Department(Base):
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, unique=True)
    employee_nums = Column(BigInteger, nullable=False, default=0)
    min_salary = Column(Float, nullable=False, default=0)
    max_salary = Column(Float, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=True)

    employees = relationship("Employee", back_populates="department")

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            employee_nums=data.get('employee_nums', 0),
            min_salary=data.get('min_salary', 0.0),
            max_salary=data.get('max_salary', 0.0)
        )

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'employee_nums': self.employee_nums,
            'min_salary': self.min_salary,
            'max_salary': self.max_salary,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    position_at_work = Column(PgEnum(PositionAtWorkEnum, name="position_at_work_enum", create_type=False), nullable=False)
    # nuit = Column(BigInteger, nullable=False, unique=True)
    # identity_card_bi = Column(String(255), nullable=False, unique=True)
    # salary = Column(Float, nullable=False, default=0)
    date_admission = Column(DateTime, nullable=False)
    state = Column(String, nullable=False)
    length_of_service = Column(Integer, nullable=True)
    # age = Column(Integer, nullable=True)
    academic_level = Column(String(255), nullable=False)
    department_id = Column(BigInteger, ForeignKey('department.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    department = relationship("Department", back_populates="employees")
    rating = relationship("EmployeeRating", back_populates="employee", cascade="all, delete", passive_deletes=True)
    users = relationship("User", secondary="user_employee", back_populates="employees", passive_deletes=True)
    working_hours = relationship("WorkingHours", back_populates="employee", cascade="all, delete", passive_deletes=True)
    progressions = relationship("Progression", back_populates="employee", cascade="all, delete", passive_deletes=True)
    
    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            position_at_work=data.get('position_at_work'),
            nuit=data.get('nuit'),
            identity_card_bi=data.get('identity_card_bi'),
            salary=data.get('salary', 0),
            date_admission=data.get('date_admission'),
            academic_level=data.get('academic_level'),
            department_id=data.get('department_id')
        )

    def to_json(self):
        return {
            'id': self.id,
            'position_at_work': self.position_at_work.name if self.position_at_work else None,
            'nuit': self.nuit,
            'identity_card_bi': self.identity_card_bi,
            'salary': self.salary,
            'date_admission': self.date_admission.isoformat() if self.date_admission else None,
            'academic_level': self.academic_level,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'department_id': self.department_id
        }


class UserEmployee(Base):
    __tablename__ = 'user_employee'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('user.id', onupdate="NO ACTION", ondelete="cascade"), nullable=False)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="cascade"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, onupdate=func.now())

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            user_id=data.get('user_id'),
            employee_id=data.get('employee_id')
        )

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'employee_id': self.employee_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
class UserContact(Base):
    __tablename__ = 'user_contact'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey('user.id', onupdate="NO ACTION", ondelete="CASCADE"), nullable=False)
    contact = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    user = relationship("User", back_populates="contacts")

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            user_id=data.get('user_id'),
            contact=data.get('contact')
        )

    def to_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'contact': self.contact,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class EmployeeRating(Base):
    __tablename__ = 'employee_rating'

    id = Column(Integer, primary_key=True, autoincrement=True)
    is_assiduous = Column(Boolean, nullable=False, default=False)
    is_collaborative = Column(Boolean, nullable=False, default=False)
    completed_goals = Column(Integer, nullable=False, default=0)
    is_punctual = Column(Boolean, nullable=False, default=False)
    work_quality_rating = Column(Integer, nullable=False, default=0)
    problem_solving_skills_rating = Column(Integer, nullable=False, default=0)
    communication_skills_rating = Column(Integer, nullable=False, default=0)
    time_management_skills_rating = Column(Integer, nullable=False, default=0)
    leadership_skills_rating = Column(Integer, nullable=False, default=0)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="cascade"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    employee = relationship("Employee", back_populates="rating")

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            is_assiduous=data.get('is_assiduous', False),
            is_collaborative=data.get('is_collaborative', False),
            completed_goals=data.get('completed_goals', 0),
            is_punctual=data.get('is_punctual', False),
            work_quality_rating=data.get('work_quality_rating', 0),
            problem_solving_skills_rating=data.get('problem_solving_skills_rating', 0),
            communication_skills_rating=data.get('communication_skills_rating', 0),
            time_management_skills_rating=data.get('time_management_skills_rating', 0),
            leadership_skills_rating=data.get('leadership_skills_rating', 0),
            employee_id=data.get('employee_id')
        )

    def to_json(self):
        return {
            'id': self.id,
            'is_assiduous': self.is_assiduous,
            'is_collaborative': self.is_collaborative,
            'completed_goals': self.completed_goals,
            'is_punctual': self.is_punctual,
            'work_quality_rating': self.work_quality_rating,
            'problem_solving_skills_rating': self.problem_solving_skills_rating,
            'communication_skills_rating': self.communication_skills_rating,
            'time_management_skills_rating': self.time_management_skills_rating,
            'leadership_skills_rating': self.leadership_skills_rating,
            'employee_id': self.employee_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Goals(Base):
    __tablename__ = 'goals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(Text, nullable=False)
    start_date = Column(DateTime, nullable=False)
    conclusion_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    status = Column(PgEnum(GoalStatusEnum), nullable=False, default=GoalStatusEnum.not_started)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    employee = relationship("Employee")
   
    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            description=data.get('description'),
            start_date=data.get('start_date'),
            conclusion_date=data.get('conclusion_date'),
            end_date=data.get('end_date'),
            status=data.get('status'),
            employee_id=data.get('employee_id')
        )

    def to_json(self):

        return {
            'id': self.id,
            'description': self.description,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'conclusion_date': self.conclusion_date.isoformat() if self.conclusion_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'status': self.status,
            'employee_id': self.employee_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class PerformanceEvaluation(Base):
    __tablename__ = 'performance_evaluation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    employee_rating_id = Column(BigInteger, ForeignKey('employee_rating.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    employee_goals_id = Column(BigInteger, ForeignKey('goals.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    feedback = Column(PgEnum(FeedbackEnum), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    employee = relationship("Employee")
    employee_rating = relationship("EmployeeRating")
    employee_goals = relationship("Goals")


    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            employee_id=data.get('employee_id'),
            employee_rating_id=data.get('employee_rating_id'),
            employee_goals_id=data.get('employee_goals_id'),
            feedback=data.get('feedback')
        )

    def to_json(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'employee_rating_id': self.employee_rating_id,
            'employee_goals_id': self.employee_goals_id,
            'feedback': self.feedback.value if self.feedback else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
class Presences(Base):
    __tablename__ = 'presences'

    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="NO ACTION"), nullable=False)
    month = Column(String(255), nullable=False)
    year = Column(Integer, nullable=False)
    presences = Column(Integer, nullable=False, default=0)
    absences = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    employee = relationship("Employee")
    
    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            employee_id=data.get('employee_id'),
            month=data.get('month'),
            year=data.get('year'),
            presences=data.get('presences', 0),
            absences=data.get('absences', 0)
        )

    def to_json(self):
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'month': self.month,
            'year': self.year,
            'presences': self.presences,
            'absences': self.absences,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class WorkingHours(Base):
    __tablename__ = 'working_hours'

    id = Column(Integer, primary_key=True, autoincrement=True)
    normal_hours = Column(Integer, nullable=False, default=0)
    overtime = Column(Integer, nullable=False, default=0)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="cascade"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    employee = relationship("Employee")

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get('id'),
            normal_hours=data.get('normal_hours', 0),
            overtime=data.get('overtime', 0),
            employee_id=data.get('employee_id')
        )

    def to_json(self):
        return {
            'id': self.id,
            'normal_hours': self.normal_hours,
            'overtime': self.overtime,
            'employee_id': self.employee_id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
    
class Progression(Base):
    __tablename__ = "progressions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(BigInteger, ForeignKey('employee.id', onupdate="NO ACTION", ondelete="cascade"), nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    employee = relationship("Employee")

    def to_json(self):
        return {
            "id": self.id,
            "employee_id": self.employee_id,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def to_model(cls, data):
        return cls(
            id=data.get("id"),
            employee_id=data.get("employee_id"),
            description=data.get("description")
        )

Base.metadata.create_all(engine)