import time

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from threading import Thread

import logger
from controler.var import *
import threading
from controler import models2
from controler import database_connector as dbc
from UI.tabLoadData import Content
data=None
table=None
len_data=None
def import_data(filepath,delimiter,table_input,label):
    print(label)
    label.config(text='Đang nạp...')
    global data
    global table
    global len_data
    print('import')
    table=table_input
    data = pd.read_csv(filepath,delimiter= delimiter,engine='python')
    len_data=len(data)
    G.len_data=len_data
def get_list_column_import():
    global table
    list1= list(data.columns.values)
    object = models2.get_table_object(table)
    list2=models2.get_list_columns(object=object)
    list3 = list(set(list1).intersection(list2))
    return list3
def commit(label):
    print('loadData.commit')
    print(str(int(G.i * 100 / G.len_data))+'%')
    dbc.DbConnector.session.commit()
    if(G.i==G.len_data):
        G.is_done=True
        print(str(int(G.i * 100 / G.len_data)) + '%')
        label.config(text='Done')
def load_data(list,label):
    global len_data
    global table
    print('loadData.load_data')
    try:
        for G.i in range(0, len_data):
            object = models2.get_table_object(table)
            for j in range(0, len(list)):
                key = list[j]
                val = data[list[j]][G.i]
                setattr(object, key, val)
                """
                print(type(getattr(object,key)))
                if type(getattr(object,key))=='int':
                    setattr(object, key, int(val))
                if type(getattr(object,key))=='float':
                    setattr(object, key, float(val))
                if type(getattr(object,key))=='str':
                    setattr(object, key, val)
                """
            dbc.DbConnector.session.add(object)
            del object
            if (G.i % 100000 == 0 or G.i == len_data-1):
                t1 = threading.Thread(target=commit(label))
                t1.start()
        return True
    except:
        return False
