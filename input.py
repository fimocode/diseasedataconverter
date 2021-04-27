import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
import database_connector as dbc
"""
engine= create_engine('mysql+pymysql://root:@localhost/disease2')
#data  = pd.read_csv("/home/minhduc/Desktop/git05/LicensePlateDetection/disease1.csv",delimiter='\t')
Session = sessionmaker(engine)
session = Session()
"""
filepath=input('Nhap filepath: ')
table = input('Nhap table: ')
map={}
n = input('Nhap so cot: ')
col = []
for i in range(0,int(n)):
    s = input('Map cot(table)->cot(file): ')
    col.append(s)
    a = col[i].split(" ")
    map[a[0]]=a[1]