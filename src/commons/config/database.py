from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from src.commons.client.config_client import ConfigClient

URL_DATABASE = ConfigClient.get_property(section='DATABASE', name='URL')

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(expire_on_commit=False, autoflush=False, bind=engine)

Base = declarative_base()
