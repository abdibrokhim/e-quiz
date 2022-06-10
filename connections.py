# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm import declarative_base
# # from sqlalchemy.orm import Session
#
#
# def get_engine():
#     engine = create_engine('sqlite:///./database.db', echo=True, future=True)
#     return engine
#
#
# def get_session():
#     session = sessionmaker(bind=get_engine())
#     return session
#
#
# def get_base():
#     Base = declarative_base()
#     return Base
