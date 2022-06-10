from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///./test.db', echo=True)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
Base = declarative_base()


# import connections
# Engine = connections.get_engine()
# Session = connections.get_session()
# Base = connections.get_base()


class User(Base):
    __tablename__ = 'USER'
    ID = Column(Integer, primary_key=True)
    FULLNAME = Column(String(50))
    NICKNAME = Column(String(50))
    PASSWORD = Column(String(50))
    OCCUPATION = Column(String(50))
    POINT = Column(Integer)

    def __repr__(self):
        return "<User(FULLNAME='%s', NICKNAME='%s', PASSWORD='%s', OCCUPATION='%s', POINT='%d')>" % (
            self.FULLNAME, self.NICKNAME, self.PASSWORD, self.OCCUPATION, self.POINT)


class Test(Base):
    __tablename__ = "TEST"
    ID = Column(Integer, primary_key=True)
    DESCRIPTION = Column(String, nullable=False)
    ANSWER = Column(String, nullable=False)

    def __repr__(self):
        return "<Test(DESCRIPTION='%s', ANSWER='%s')>" % (
            self.DESCRIPTION, self.ANSWER)

    # Base.metadata.create_all(engine)


def update_table():
    pass
    # MOVE TWO ABOVE CLASSES WITHIN THIS FUNCTION IN ORDER TO CREATE TABLES
    # THAN MOVE OUT WITHIN THIS FUNCTION AGAIN, IT'S INITIAL PLACE
    # OTHERWISE IT WILL NOT WORK PROPERLY
