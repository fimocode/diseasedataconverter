from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from logger import logging
from settings import DBConfig, RETRY_WAIT_SEC
from func_retrying import DbConnectorRetrying
from models import Image

class DbConnector:
    session = None

    def __init__(self):
        self.engine = create_engine(
            "mysql://{db_user}:{db_password}@{db_host}/{db_name}?charset={db_charset}".format(
                db_user=DBConfig.DB_USERNAME,
                db_password=DBConfig.DB_PASSWORD,
                db_host=DBConfig.DB_HOSTNAME,
                db_name=DBConfig.DB_NAME
            ), pool_pre_ping=True)
        Session = sessionmaker(self.engine)
        self.session = Session()

    def get_session(self):
        return self.session

    def exec_query(self, obj, **params):
        with self.engine.connect() as conn:
            return conn.execute(obj, **params)

    def exec_query_without_raise(self, obj, **params):
        return DbConnectorRetrying.run_query_without_raise(self.session, self.exec_query, 3,
                                                           obj, **params)

    def load_one_record(self, model):
        return self.session.query(model).one_or_none()

    def exec_load_one_record_without_raise(self, model):
        return DbConnectorRetrying.run_query_without_raise(self.session, self.load_one_record, 3, model)

    def load_by_batch(self, model, _filter, _order, _limit):
        return self.session.query(model).filter(_filter).order_by(_order).limit(_limit).all()

    def exec_load_by_batch_without_raise(self, model, _filter, _order, _limit):
        results = DbConnectorRetrying.run_query_without_raise(self.session, self.load_by_batch, 3,
                                                              model, _filter, _order, _limit)
        return results if results else []

    def updated_one_record(self, model):
        model.updated_at = datetime.now()
        self.session.commit()

    def exec_update(self, model):
        DbConnectorRetrying.run_query(self.session, self.updated_one_record, 3, RETRY_WAIT_SEC, model)

    def update_by_batch(self, model, mappings):
        for idx, obj in enumerate(mappings):
            obj['updated_at'] = datetime.now()
            mappings[idx] = obj
        self.session.bulk_update_mappings(model, mappings)
        self.session.commit()

    def exec_update_by_batch(self, model, mappings):
        DbConnectorRetrying.run_query(self.session, self.update_by_batch, 3, RETRY_WAIT_SEC, model, mappings)

    def update_by_bulk(self, objects, return_defaults=False):
        for idx, obj in enumerate(objects):
            obj.updated_at = datetime.now()
            objects[idx] = obj
        self.session.bulk_save_objects(objects, return_defaults=return_defaults)
        self.session.commit()
        return objects

    def exec_update_by_bulk(self, objects, retry_time=3, retry_seconds=RETRY_WAIT_SEC, return_defaults=False):
        return DbConnectorRetrying.run_query(self.session, self.update_by_bulk, retry_time, retry_seconds, objects, return_defaults)

    def create_record(self, instance):
        instance.created_at = datetime.now()
        instance.updated_at = datetime.now()
        self.session.add(instance)
        self.session.commit()
        return instance

    def exec_create(self, instance):
        return DbConnectorRetrying.run_query(self.session, self.create_record, 3, RETRY_WAIT_SEC, instance)

    def create_by_batch(self, objects, return_defaults=False):
        for idx, obj in enumerate(objects):
            obj.updated_at = datetime.now()
            obj.created_at = datetime.now()
            objects[idx] = obj
        self.session.bulk_save_objects(objects, return_defaults=return_defaults)
        self.session.commit()
        return objects

    def exec_create_by_batch(self, objects, return_defaults=False):
        return DbConnectorRetrying.run_query(self.session, self.create_by_batch, 3, RETRY_WAIT_SEC, objects, return_defaults)

    def catch_exception(self, e):
        logging.error("DatabaseConnector error. Catch exception with traceback")
        logging.exception(e)
        self.session.rollback()

    def close(self):
        self.session.commit()
        self.session.close()
        self.engine.dispose()
