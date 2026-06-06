import todo.models

from sqlalchemy import create_engine

engine = create_engine("sqlite:///todo.db", echo=True)