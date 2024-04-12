import mysql.connector


dataBase = mysql.connector.connect(
    host="localhost",
      user="root",
      password='king007'
      )

cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE CRM")

print("all done !")


