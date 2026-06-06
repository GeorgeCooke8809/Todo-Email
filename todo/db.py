from main import DATABASE_URL, DEBUGGING_STATE
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

engine = create_engine(DATABASE_URL, echo=DEBUGGING_STATE)

class Base(DeclarativeBase):
    pass