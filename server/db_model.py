from sqlalchemy import create_engine, Column, Integer, String, Sequence, engine, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

Base = declarative_base()


class DatabaseModel:
    def __init__(self):
        self.engine = create_engine('postgresql+pg8000://postgres:Action500@144.172.153.80:50000/postgres', echo=True)
        self.Session = sessionmaker()
        self.Session.configure(bind=self.engine)
        Base.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        return self.Session()


class GarbageLocation(Base):
    __tablename__ = 'garbage_location'

    id = Column(Integer, Sequence('garbage_location_seq'), primary_key=True)
    location_name = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    date = Column(Date)
    image_url = Column(String)
    pollution_level = Column(Integer)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

