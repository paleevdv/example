from sqlalchemy import BigInteger, Column, DateTime, Sequence, VARCHAR, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from settings import DB_TABLE_NAME, DB_SEQUENCE_NAME

Base = declarative_base()

class ExampleModel(Base):

    __tablename__ = DB_TABLE_NAME

    id = Column(BigInteger, Sequence(DB_SEQUENCE_NAME), primary_key=True, index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    name = Column(VARCHAR(255))
    data = Column(Text)
