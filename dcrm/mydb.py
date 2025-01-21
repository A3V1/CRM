import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='107gaming',
    database='coldplay'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE coldplay")

print("done")

