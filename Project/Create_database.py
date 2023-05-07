import mysql.connector

mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   password="30Divyansh@"
)

c = mydb.cursor()
c.execute("CREATE DATABASE PetrolPump_Management")