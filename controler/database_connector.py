from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from logger import logging
# from settings import DBConfig, RETRY_WAIT_SEC
#from models import Image

class DbConnector:
    session = None
    engine = None
    def __init__(self):
        pass
    #ham connect
    @staticmethod
    def connectsql(host,port,username,password,database):
        try:
            DbConnector.engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(username,password,host,port,database))
            Session = sessionmaker(DbConnector.engine)
            DbConnector.session = Session()
            DbConnector.engine.connect()
            if DbConnector.engine!=None:
                return True
        except:
            return False
    def get_session(self):
        return self.session
    def updated_one_record(self, model):
        model.updated_at = datetime.now()
        self.session.commit()


    def update_by_batch(self, model, mappings):
        for idx, obj in enumerate(mappings):
            obj['updated_at'] = datetime.now()
            mappings[idx] = obj
        self.session.bulk_update_mappings(model, mappings)
        self.session.commit()

    @staticmethod
    def close():
        DbConnector.session.commit()
        DbConnector.session.close()
        DbConnector.engine.dispose()
