from sqlalchemy import create_engine, Column, Integer, String, Sequence, engine
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


class GarbageRemovalEvent(Base):
    __tablename__ = 'garbage_removal_event'

    id = Column(Integer, Sequence('garbage_removal_event_seq'), primary_key=True)
    location_name = Column(String)
    latitude = Column(Integer)
    longitude = Column(Integer)
    date = Column(String)
    image_url = Column(String)
    pollution_level = Column(Integer)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    # def __repr__(self) -> str:
    #     return (
    #         "location_name: {}, "
    #         "latitude: {}, "
    #         "longitude: {}, "
    #         "date: {}, "
    #         "image_url: {}, "
    #         "pollution_level: {}".format(
    #             self.location_name, self.latitude, self.longitude, self.date, self.image_url, self.pollution_level
    #         )
    #     )
