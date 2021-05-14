#!/usr/bin/env python
import sqlite3, urllib2, json, os, time, psutil

def TempVar():
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=","").replace("'C","").replace("\n",""))

def main():
    Temperature = TempVar()
    CPU = psutil.cpu_percent()
    my_query = 'INSERT INTO CPU(Datetime, TempC, CPU) VALUES(CURRENT_TIMESTAMP, %s,%s);' %(Temperature,CPU)
    try:
        connection = sqlite3.connect('/home/pi/CPUData/CPUdatalog.db',isolation_level=None)
        cursor = connection.cursor()
        cursor.execute(my_query)
        query_results = cursor.fetchone()
        my_response = 'Inserted temp = %s and CPU usage = %s successfully' % (Temperature,CPU)
    except sqlite3.Error, e:
        my_response = "There is an error %s:" % (e)
    finally:
        print my_response
        connection.close()

if __name__ == "__main__":
    main()
