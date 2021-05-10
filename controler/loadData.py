import time
from sqlalchemy import update
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from threading import Thread
import logger
from controler.var import *
import threading
from controler import models2
from controler import database_connector as dbc
data=None
table=None
len_data=None
def import_data(filepath,delimiter,table_input):
    try:
        global data
        global table
        global len_data
        table=table_input
        data = pd.read_csv(filepath,delimiter= delimiter,engine='python')
        len_data=len(data)
        G.len_data=len_data
        return True
    except:
        return False
def get_list_column_import():
    global table
    list1= list(data.columns.values)
    object = models2.get_table_object(table)
    list2=models2.get_list_columns(object=object)
    list3 = list(set(list1).intersection(list2))
    return list3
def load_data(list):
    list_null = ['NULL', 'NA', 'nan', '', 'NaN']
    global len_data
    global table
    print('loadData.load_data')
    try:
        for G.i in range(0, len_data):
            object = models2.get_table_object(table)
            for j in range(0, len(list)):
                key = list[j]
                val = data[list[j]][G.i]
                #if val !='NA' and val != "NULL" and val != '':
                if val not in list_null:
                    setattr(object, key, val)
            dbc.DbConnector.session.add(object)
            del object
            if (G.i % 100000 == 0 or G.i == len_data-1):
                print(str(int(G.i * 100 / G.len_data)) + '%')
                dbc.DbConnector.session.commit()
        G.result_import_data=  True
    except:
        G.result_import_data=  True
#method update du lieu
def update_data(key,list_column,table):
    list_null=['NULL','NA','nan','','NaN']
    global data
    global len_data
    cluster = ''
    str1 = f"update {table} set "
    try:
        for G.j in range(0,G.len_data):
            str2 = ""
            str3 = f" where {key}='{data[key][G.j]}';"
            for i in range(0, len(list_column)):
                if i == len(list_column) - 1:
                    #if data[list_column[i]][G.j] == 'NULL' or data[list_column[i]][G.j] == 'NA' or data[list_column[i]][G.j] == '':
                    if str(data[list_column[i]][G.j]) in list_null:
                        str2 = str2 + f"{list_column[i]} = NULL"
                    else:
                        str2 = str2 + f"{list_column[i]} = '{data[list_column[i]][G.j]}'"
                else:
                    #if data[list_column[i]][G.j] == 'NULL' or data[list_column[i]][G.j] == 'NA' or data[list_column[i]][G.j] == '':
                    if str(data[list_column[i]][G.j]) in list_null:
                        str2 = str2 + f"{list_column[i]} = NULL,"
                    else:
                        str2 = str2 + f"{list_column[i]} = '{data[list_column[i]][G.j]}',"
            query = str1 + str2 + str3
            dbc.DbConnector.session.execute(query)
        G.result_update_data = True
    except:
        G.result_update_data = False
