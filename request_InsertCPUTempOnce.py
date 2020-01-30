#!/usr/bin/env python
import sqlite3
import urllib2
import json
import os
import time

#def measure_temp():
#        temp = os.popen("vcgencmd measure_temp").readline()
#        return (temp.replace("temp=","").replace("'C",""))


def main():
    Room = 1
    #time.sleep(1)
    #Temperature = measure_temp() 
    my_query = 'INSERT INTO Temperature(RoomID,TemperatureC,Datetime,CPU) VALUES(%s,"",CURRENT_TIMESTAMP,"");' %(Room)
    try:
        connection = sqlite3.connect('/home/pi/database/control.db',isolation_level=None)
        cursor = connection.cursor()
        cursor.execute(my_query)
        query_results = cursor.fetchone()
        my_response = '_FromReBoot_Inserted Null for room %s' % (Room)
    except sqlite3.Error, e:
        my_response = "_FromReBoot_There is an error %s:" % (e)
    finally:
        print my_response
        connection.close()

if __name__ == "__main__":
    main()

