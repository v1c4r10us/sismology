import requests
import pandas as pd
from config.db import conn
import time

# Cycle for country: get_last_quake --> check_not_exist --> save_mongo

def get_last_quake(country):
    countries={'usa':'https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&orderby=time','japan':'https://www.jma.go.jp/bosai/quake/data/list.json','chile':'https://api.xor.cl/sismo/recent'}
    #Only for USA
    df=pd.read_csv(countries[country])
    df=df[['time','latitude','longitude','depth','mag','place']] #Valid fields
    df=df.head(1) #Top 1 order by time
    df=df.squeeze() #Serializing
    quake={'time':df['time'], 'latitude':df['latitude'], 'longitude':df['longitude'], 'depth':df['depth'], 'mag':df['mag'], 'place':df['place'], 'country':country} #Typing for mongo
    log='' #Logs for insertions
    if check_not_exist(df['time'],country):
        save_mongo(quake)
        log='1 new quake added'
    else:
        log='0 new quake added'
    return log
        
def check_not_exist(time, country): #Verify if quake exists for 'country'
    if conn.sismology.quakes.find_one({'time':time,'country':country})!=None:
        return False 
    else:
        return True
        
def save_mongo(quake): #Save into mongo latest quake    
    #Inserting document
    db=conn['sismology']
    collection=db['quakes']
    collection.insert_one(quake)

start=time.time()
print(get_last_quake('usa'))
stop=time.time()
print('--Elapsed--> ', stop-start)