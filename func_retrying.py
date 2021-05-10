import sqlalchemy as SA
from logger import logging
from time import sleep

class DbConnectorRetrying:
    @staticmethod
    def warning(session, e):
        logging.warning("Database connection has problem. Retrying...: %s" % e)
        session.rollback()

    @staticmethod
    def catch_exception(session, e):
        logging.error("DbConnectorRetrying error. Catch exception with traceback")
        logging.exception(e)
        session.rollback()

    @staticmethod
    def run_query(session, f, attempts=3, retry_seconds=0.5, *args):
        expt = None
        while attempts > 0:
            attempts -= 1
            try:
                return f(*args)
            except SA.exc.DBAPIError as exc:
                expt = exc
                if attempts > 0 and exc.connection_invalidated:
                    DbConnectorRetrying.warning(session, exc)
                elif attempts <= 0:
                    session.rollback()
                    raise
                elif not exc.connection_invalidated:
                    DbConnectorRetrying.warning(session, exc)
            except SA.orm.exc.StaleDataError as exc:
                expt = exc
                DbConnectorRetrying.warning(session, exc)
                sleep(retry_seconds)
            except Exception:
                session.rollback()
                raise
        if attempts <= 0:
            raise expt

    @staticmethod
    def run_query_without_raise(session, f, attempts=3, *args):
        while attempts > 0:
            attempts -= 1
            try:
                return f(*args)
            except SA.exc.DBAPIError as exc:
                if attempts > 0 and exc.connection_invalidated:
                    DbConnectorRetrying.warning(session, exc)
                else:
                    DbConnectorRetrying.warning(session, exc)
            except Exception as e:
                DbConnectorRetrying.catch_exception(session, e)
        return None
