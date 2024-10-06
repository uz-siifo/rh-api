from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from settings import Settings

Base = declarative_base()
engine = create_engine(Settings().DATABASE_URL)
Base.metadata.create_all(engine)