import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="joy",
    database='menagerie'
)


mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for tb in mycursor:
    print(tb)
    
mydb.commit()

