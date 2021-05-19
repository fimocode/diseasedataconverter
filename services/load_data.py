import threading
import datetime
import time
import tkinter as tk
import pandas as pd
from controlers.var import *
from models import database_connector as dbc, models
from UI import tab_import_data as tid
from UI import tab_update_data as tud
import numpy as np
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
    object = models.get_table_object(table)
    list2= models.get_list_columns(object=object)
    list3 = list(set(list1).intersection(list2))
    return list3
def load_data(list,id_start):
    try:
        list_null = ['NULL', 'NA', 'nan', '', 'NaN']
        global len_data
        global table
        G.record_start=id_start
        G.time_start=datetime.datetime.utcnow()
        for G.i in range(id_start, len_data):
            object = models.get_table_object(table)
            for j in range(0, len(list)):
                key = list[j]
                val = data[list[j]][G.i]
                if str(val) not in list_null:
                    setattr(object, key, val)
            dbc.DbConnector.session.add(object)
            del object
            if (G.i % 1000 == 0 or G.i == len_data-1):
                dbc.DbConnector.conmmitsql()
                tid.Content.result_import.config(text=str(round(G.i * 100 / (G.len_data-1), 4)) + '%')
            if G.i == (G.len_data - 1):
                tid.Content.reset_button['state'] = tk.NORMAL
            if(G.active==False):
                break
            G.record_end = G.i
            G.time_end = datetime.datetime.utcnow()
        tid.Content.num_record_lb.config(text=f'Import {G.record_end - G.record_start + 1} records')
        tid.Content.num_time_lb.config(text=f'Total {str((G.time_end - G.time_start).total_seconds())} seconds')
        G.result_import_data=  True
    except SystemExit:
        print('stop import')
    except:
        tid.Content.result_import.config(text="Error import data!")
        G.result_import_data=  False
#method update du lieu
def update_data(key,list_column,table,id_start):
    try:
        list_null=['NULL','NA','nan','','NaN']
        global data
        global len_data
        G.j = id_start
        G.record_start = id_start
        G.time_start = datetime.datetime.utcnow()
        str1 = f"update {table} set "
        for G.j in range(id_start,G.len_data):
            str2 = ""
            str3 = f" where {key}='{data[key][G.j]}';"
            for i in range(0, len(list_column)):
                if i == len(list_column) - 1:
                    if str(data[list_column[i]][G.j]) in list_null:
                        str2 = str2 + f"{list_column[i]} = NULL"
                    else:
                        str2 = str2 + f"{list_column[i]} = '{data[list_column[i]][G.j]}'"
                else:
                    if str(data[list_column[i]][G.j]) in list_null:
                        str2 = str2 + f"{list_column[i]} = NULL,"
                    else:
                        str2 = str2 + f"{list_column[i]} = '{data[list_column[i]][G.j]}',"
            query = str1 + str2 + str3
            dbc.DbConnector.executesql(query)
            if (G.j % 1000 == 0 or G.j == len_data - 1):
                tud.Content.result_update.config(text=str(round(G.j * 100 / (G.len_data-1), 4)) + '%')
            if G.j == (G.len_data - 1):
                tud.Content.reset_button['state'] = tk.NORMAL
            if G.active == False:
                break
            G.record_end = G.j
            G.time_end = datetime.datetime.utcnow()
        tud.Content.num_record_lb.config(text=f'Import {G.record_end - G.record_start + 1} records')
        tud.Content.num_time_lb.config(text=f'Total {str((G.time_end - G.time_start).total_seconds())} seconds')
        G.result_update_data = True
    except SystemExit:
        print('stop update')
    except:
        tud.Content.result_update.config(text="Error update data!")
        G.result_update_data = False

