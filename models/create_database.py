import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import model
from models import database_connector as dbc
from settings import DBConfig

username = DBConfig.DB_USERNAME
password = DBConfig.DB_PASSWORD
host = DBConfig.DB_HOSTNAME
port = "3306"
database = DBConfig.DB_NAME or "diseasetest"
engine= create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(username,password,host,port,database))
Session = sessionmaker(engine)
session = Session()
model.Base.metadata.create_all(engine)

session.commit()
engine.dispose()
