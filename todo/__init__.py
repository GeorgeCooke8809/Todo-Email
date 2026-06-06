import todo.models
from main import DATABASE_URL

from sqlalchemy import create_engine

engine = create_engine(DATABASE_URL, echo=True)