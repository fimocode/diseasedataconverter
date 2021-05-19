from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbConnector:
    session = None
    engine = None
    con = None
    def __init__(self):
        pass
    #ham connect
    @staticmethod
    def connectsql(host,port,username,password,database):
        try:
            DbConnector.engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(username,password,host,port,database))
            Session = sessionmaker(DbConnector.engine)
            DbConnector.session = Session()
            DbConnector.conn = DbConnector.engine.connect()
            if DbConnector.engine!=None:
                return True
        except:
            return False
    @staticmethod
    def conmmitsql():
        try:
            DbConnector.session.commit()
        except:
            print('stop commit')
            raise SystemExit

    @staticmethod
    def executesql(sql):
        try:
            DbConnector.session.execute(sql)
        except:
            print('stop update')
            raise SystemExit
    @staticmethod
    def close():
        try:
            if DbConnector.session!=None:
                DbConnector.session.close()
            if DbConnector.engine !=None:
                DbConnector.engine.dispose()
        except:
            print('close')