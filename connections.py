from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


def get_engine():
    engine = create_engine('sqlite:///./database.db', echo=True)
    return engine


def get_session():
    session = sessionmaker(bind=get_engine())
    return session


def get_base():
    base = declarative_base()
    return base