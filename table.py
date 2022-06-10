# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import declarative_base
# from sqlalchemy import Sequence
#
# engine = create_engine('sqlite:///./database.db', echo=True)
# Session = sessionmaker(bind=engine)
# Base = declarative_base()
# Column(Integer, Sequence('user_id_seq'), primary_key=True)
from sqlalchemy import Column, Integer, String
import connections

Engine = connections.get_engine()
Session = connections.get_session()
Base = connections.get_base()


class User(Base):
    __tablename__ = 'USER'
    ID = Column(Integer, primary_key=True)
    FULLNAME = Column(String(50))
    NICKNAME = Column(String(50))
    PASSWORD = Column(String(50))
    OCCUPATION = Column(String(50))
    POINT = Column(Integer)

    def __init__(self, FULLNAME, NICKNAME, PASSWORD, OCCUPATION, POINT):
        self.FULLNAME = FULLNAME
        self.NICKNAME = NICKNAME
        self.PASSWORD = PASSWORD
        self.OCCUPATION = OCCUPATION
        self.POINT = POINT


class Test(Base):
    __tablename__ = "TEST"
    ID = Column(Integer, primary_key=True)
    DESCRIPTION = Column(String, nullable=False)
    ANSWER = Column(String, nullable=False)

    def __init__(self, ID, DESCRIPTION, ANSWER):
        self.ID = ID
        self.DESCRIPTION = DESCRIPTION
        self.ANSWER = ANSWER


    # Base.metadata.create_all(Engine)