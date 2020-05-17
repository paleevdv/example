from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from settings import DATABASE_URL

DB_ENGINE = create_engine(DATABASE_URL)
DB_SESSION = scoped_session(sessionmaker(bind=DB_ENGINE, autocommit=False))

from .model import ExampleModel

