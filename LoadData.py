import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd= "root",
)

cursor = db.cursor()


cursor.execute("USE IncidentDatabase")
cursor.execute("DROP TABLE TestData")
cursor.execute("""CREATE TABLE TestData(
                id INT PRIMARY KEY AUTO_INCREMENT,
                date VARCHAR(255) ,
                incident_type VARCHAR(255),
                location VARCHAR(255),
                longitude FLOAT,
                latitude FLOAT,
                description VARCHAR(1000),
                FILE_URI VARCHAR(255)
            )""")

count = 0
with open('data_long.csv', 'r') as dataFile:
    headers = dataFile.readline().split(',')
    count = 0
    for line in dataFile:
        data = line.split(',')

        if(len(data) > 8):
            cursor.execute("""
                INSERT INTO TestData (
                    date,
                    incident_type, 
                    location,
                    longitude, 
                    latitude, 
                    description, 
                    FILE_URI
                )
                Values (
                    '{}', '{}', '{}', '{}', '{}', '{}', '{}'
                )
            """.format(
                data[0],
                data[2],
                data[-1],
                float(data[6][1:-1]),
                float(data[7][1:-1]),
                data[5],
                data[3]

            ))
        else:
            cursor.execute("""
                INSERT INTO TestData (
                    date,
                    incident_type, 
                    location,
                    longitude, 
                    latitude, 
                    description, 
                    FILE_URI
                )
                Values (
                    '{}', '{}', '{}', '{}', '{}', '{}', '{}'
                )
            """.format(
                data[0],
                data[2],
                data[-1],
                float(data[5][1:-1]),
                float(data[6][1:-1]),
                data[4],
                data[3]

            ))
        db.commit()
