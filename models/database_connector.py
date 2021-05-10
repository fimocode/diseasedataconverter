from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from logger import logging
from settings import DBConfig

class DbConnector:
    session = None
    engine = None
    def __init__(self):
        pass
    #ham connect
    @staticmethod
    def connectsql(host,port,username,password,database):
        try:
            DbConnector.engine = create_engine(
                "mysql://{db_user}:{db_password}@{db_host}/{db_name}".format(
                    db_user=DBConfig.DB_USERNAME,
                    db_password=DBConfig.DB_PASSWORD,
                    db_host=DBConfig.DB_HOSTNAME,
                    db_name=DBConfig.DB_NAME,
                ), pool_pre_ping=True)
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
