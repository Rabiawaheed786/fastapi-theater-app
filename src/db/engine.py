# engine.py
from sqlmodel import create_engine, SQLModel, Session
import src.model as model


database_url = "sqlite:///database.db"
engine = create_engine(database_url, echo=True)


# create table
def create_tables():
    SQLModel.metadata.create_all(engine) 


# open/close DB connection
def get_session():
   with Session(engine) as session:
       yield session