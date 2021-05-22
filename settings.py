import os
import ast
import sys

from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=str(env_path))

class DBConfig:
    DB_USERNAME = os.getenv('DATABASE_USERNAME', 'skrc')
    DB_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DB_HOSTNAME = os.getenv('DATABASE_HOSTNAME')
    DB_NAME = os.getenv('MAIN_DATABASE_NAME')
    DB_CHARSET = os.getenv('DATABASE_CHARSET', 'utf8')
    DB_PORT = int(os.getenv('DB_PORT', 3306))

pandas_limit_read_csv = int(os.getenv('PANDAS_LIMIT_READ_CSV', 1))
import_data_path = os.getenv('IMPORT_DATA_PATH', '/home/buinhatduy/workspaces/diseasedataconverter/data')
