import psycopg2
from decouple import config
from psycopg2 import DatabaseError
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, create_engine, Date

Base = declarative_base()
def get_connection():
    try:
        return psycopg2.connect(
            host = config('PGSQL_HOST'),
            user = config('PGSQL_USER'),
            password = config('PGSQL_PASSWORD'),
            database = config('PGSQL_DATABASE')
        )
    except DatabaseError as ex:
        raise ex

class StudentForm(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key = True)
    carnet = Column(String, nullable = False)
    fullname = Column(String, nullable = False)
    address = Column(String, nullable = False)
    gender = Column(String, nullable = False)
    phone_number = Column(String, nullable = False)
    birth_date = Column(String, nullable = False)
    career = Column(String, nullable = False)
    genre= Column(String, nullable = False)
    ins_date = Column(Date, nullable = False)
    part_date = Column(Date, nullable = False)
    age = Column(Integer, nullable = False)

engine = create_engine('postgresql://postgres:12345@localhost/api_universidad')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
