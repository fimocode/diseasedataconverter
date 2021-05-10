import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models2
import database_connector as dbc
username = "root"
password = ""
host = "localhost"
port = "3306"
database = "diseasetest"
engine= create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(username,password,host,port,database))
Session = sessionmaker(engine)
session = Session()
models2.Base.metadata.create_all(engine)

session.commit()
engine.dispose()