from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

username = "minhduc180699"
password = "99916081"
host = "localhost"
#host = "54.179.16.156"
port = "3306"
database = "idb"
engine= create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(username,password,host,port,database))
Session = sessionmaker(engine)
session = Session()
models.Base.metadata.create_all(engine)

session.commit()
engine.dispose()