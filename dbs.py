import mysql.connector
import os

# CONNECT TO THE DATABASE LOCALLY
connect_sql = mysql.connector.connect(
    host="localhost",
    user=os.environ["USERDB"],
    password=os.environ["PSW"],
    database="PassWords"
)

print("connected to mysql successfully brother")

mycursor = connect_sql.cursor()

# FUNCTION TO SHOW DATABASES
def GetDbs():
    mycursor.execute("SHOW DATABASES")
    for db in mycursor:
        print(db)

# FUNCTION TO INSERT THE VALUES PASSWORD AND APP IN THE GUI
def propasswd(value_1, value_2):
    sql = "INSERT INTO Psswd (program, password) VALUES (%s, %s)"
    val = (value_1, value_2)
    mycursor.execute(sql, val)
    connect_sql.commit()
    print(mycursor.rowcount, "record inserted.")

# FUNCTION TO RETRIEVE THE PASSWORD OF A PROGRAM
def search_program(program):
    mycursor.execute("SELECT password FROM Psswd where program='{}'".format(program))
    resul=mycursor.fetchone()
    return resul

# search_program("brigeth")
