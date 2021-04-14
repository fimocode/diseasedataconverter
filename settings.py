import os
import ast
import sys

from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=str(env_path))

class DBConfig:
    DB_USERNAME = os.getenv('DATABASE_USERNAME')
    DB_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DB_HOSTNAME = os.getenv('DATABASE_HOSTNAME')
    DB_NAME = os.getenv('DATABASE_NAME')
    DB_CHARSET = os.getenv('DATABASE_CHARSET')