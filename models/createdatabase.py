from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

username = ""
password = ""
host = ""
port = ""
database = ""
engine= create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(username,password,host,port,database))
Session = sessionmaker(engine)
session = Session()
models.Base.metadata.create_all(engine)

session.commit()
engine.dispose()