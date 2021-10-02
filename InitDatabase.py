import mysql.connector

import os
from dotenv import load_dotenv

load_dotenv()



if os.environ.get('DB_NAME') == None:
    db= mysql.connector.connect(
        host    =   os.environ.get('HOST'),
        user    =   os.environ.get('DB_USERNAME'),
        passwd  =   os.environ.get('DB_PASSWORD')
    )
    

    dbcursor = db.cursor()
    dbcursor.execute("DROP DATABASE IncidentDatabase")
    dbcursor.execute("CREATE DATABASE IncidentDatabase")
    dbcursor.execute("USE IncidentDatabase")
    dbcursor.execute("CREATE TABLE Incidents(IncidentID INT PRIMARY KEY AUTO_INCREMENT)")
    
    with open('.env', 'a') as env_file:
        env_file.write('DB_NAME=IncidentDatabase\nTABLE_NAME=Incidents\n')
