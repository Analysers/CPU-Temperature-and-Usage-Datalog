![CPU Temperature and CPU Usage DataLog](https://user-images.githubusercontent.com/52040368/72912970-e1ead700-3d55-11ea-8e50-8a1d1476c45e.png)

# TREE:
```
│   control.db                 --> Database    :   │ID│RoomID│TemperatureC│Datetime │ 
│   Flask_Data_fetching.py      --> Server py  :   in: <IP:port> ; <IP:port>/graph  │ Out : selectDB->Application/json ; http /text 
│   request_InsertCPUTemp.py    --> Insert Temperature every 1 minute              : Insert Temp loop
│   request_InsertCPUTempOnce.py--> Insert the discontinuity of Data each startup  : Insert Null once   
│
└───templates
        CanvasJS-Json-Data-Api-Ajax-Chart - Copy.html
```


# DataFlow : 
```
insert process :
    corn job :
    @reboot sudo python /home/pi/database/request_InsertCPUTempOnce.py >> /home/pi/database/log.txt   # Insert Null once
    * * * * * sudo python /home/pi/database/request_InsertCPUTemp.py   >> /home/pi/database/log.txt   # Insert Temp loop
Select process :
* jSON :
    in     : <IP:port> >> server.py : SelectDB[JSON] >> 
    Return : Application/json
* /graph :
    in     : <IP:port>/graph  >> server.py >> templates/.html : Ajax(server.py, fct(jsonData){Chart})
    Return : Application/text
```

# DATABASE: 
```
pi@rasNab:~/database $ sqlite3 control.db
SQLite version 3.16.2 2017-01-06 16:32:41
Enter ".help" for usage hints.
sqlite> select * From RoomDetails ;
1|Library
sqlite> select * From Temperature ;
1|1|222.0|2019-05-19 12:55:38
2|1|222.0|2019-05-24 13:46:47       //   ID │ RoomID │TemperatureC│ Datetime
                                    //    3 │    1   │     51.5   │2019-05-24 14:17:55
4|1|51.5|2019-05-24 14:18:05
5|1|51.5|2019-05-24 14:18:09
6|1|51.5|2019-05-24 14:18:14
7|1|51.0|2019-05-31 09:39:51
8|1|49.4|2019-06-05 06:37:08
sqlite> .quit

>CREATE TABLE Temperature (ID INTEGER PRIMARY KEY AUTOINCREMENT,
RoomID INTEGER, TemperatureC FLOAT(8), Datetime DATETIME, FOREIGN KEY(RoomID) REFERENCES RoomDetails(ID))

>CREATE TABLE RoomDetails (ID INTEGER PRIMARY KEY AUTOINCREMENT,
Room VARCHAR(25))

```
```
$ sqlite3 control.db

sqlite> .tables
RoomDetails  Temperature

sqlite> .schema
CREATE TABLE RoomDetails (ID INTEGER PRIMARY KEY AUTOINCREMENT,
Room VARCHAR(25));
CREATE TABLE Temperature (ID INTEGER PRIMARY KEY AUTOINCREMENT,
RoomID INTEGER, TemperatureC FLOAT(8), Datetime DATETIME, FOREIGN KEY(RoomID) REFERENCES RoomDetails(ID));
```
# Launch the server from host :
```
$ python3 2.1_Data_fetching.py
```
# Clien's requests : 
HTTP(HTML) Request : `http://rasnab.mshome.net:5000/graph `   
HTTP(Json) Request : `http://rasnab.mshome.net:5000/`
