import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from threading import Thread
import threading
import models2
import input
import database_connector as dbc
engine= create_engine('mysql+pymysql://root:@localhost/diseasetest')
data  = pd.read_csv(input.filepath,delimiter='\t')
Session = sessionmaker(engine)
session = Session()
len_data=len(data)
def initObject():
    if input.table == "Country":
        return models2.Country()
    if input.table == "Disease":
        return models2.Disease()
    if input.table == "GeoLocation":
        return models2.GeoLocation()
    if input.table == "Species":
        return models2.Species()
    if input.table == "ProductionType":
        return models2.ProductionType()
    if input.table == "Establishment":
        return models2.Establishment()
    if input.table == "SubUnit":
        return models2.SubUnit()
    if input.table == "Animal":
        return models2.Animal()
    if input.table == "DiseaseDetection":
        return models2.DiseaseDetection()
    if input.table == "MonitoringData":
        return models2.MonitoringData()
def commit():
    session.commit()
for i in range(0,len_data):
    object = initObject()
    for j in range(0,len(input.map)):
        key = list(input.map.keys())[j]
        val = data[list(input.map.values())[j]][i]
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
    session.add(object)
    del object
    if(i%100000==0 or i==len_data):
        print(f"{int(i*100/len_data)}%")
        t1 = threading.Thread(target=commit())
        t1.start()
session.close()
engine.dispose()
print('done')

