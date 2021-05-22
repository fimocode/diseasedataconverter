import time
import datetime
from shutil import copyfile
import subprocess


import pandas as pd

from settings import pandas_limit_read_csv, import_data_path

data=None
to_filepath=None
delimiter_file = None
ts = time.time()

def load_file(filepath, delimiter):
    try:
        global data
        global to_filepath
        global delimiter_file
        delimiter_file = delimiter
        new_data_name = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S')
        to_filepath = f'{import_data_path}/{new_data_name}.csv'
        with open(to_filepath, 'w'): pass
        copyfile(filepath, to_filepath)
        data = pd.read_csv(filepath, delimiter= delimiter_file, engine='python', nrows=pandas_limit_read_csv)
        return True
    except:
        return False


def get_list_column():
    return list(data.columns.values)


def convert(column_list):
    global data
    global delimiter_file
    try:
        new_columns = ','.join(column_list)
        subprocess.call(f"sed -i '1,1d' {to_filepath}", shell=True)
        subprocess.call(f"sed -i '1s;^;{new_columns}\\n;' {to_filepath}", shell=True)
        return to_filepath
    except SystemExit:
        exit(0)
    except:
        return False
