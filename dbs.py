import mysql.connector
import os
from mysql.connector import errorcode

# CONNECT TO THE DATABASE LOCALLY
connect_sql = mysql.connector.connect(
    host="localhost",
    user=os.environ["USERDB"],
    password=os.environ["PSW"],
    database="PassWords"
)

print("connected to mysql successfully to the database")

mycursor = connect_sql.cursor(buffered=True)

# If user exists return 0
def does_exist(program):
    try:
        existing_program = mycursor.execute('SELECT exists (SELECT program FROM Psswd WHERE program="%s")' % (program))
        existing_program = mycursor.fetchone()
        # print(res[0])
        return existing_program[0]
    except errors.ProgrammingError as e:
        return "error is {}".format(e)
    connect_sql.close()



# FUNCTION TO INSERT THE VALUES PASSWORD AND APP IN THE GUI
def propasswd(value_1, value_2):
    sql = "INSERT INTO Psswd (program, password) VALUES (%s, %s)"
    val = (value_1, value_2)
    mycursor.execute(sql, val)
    connect_sql.commit()
    print(mycursor.rowcount, "record inserted.")
    connect_sql.close()


# FUNCTION TO RETRIEVE THE PASSWORD OF A PROGRAM
def search_program(program):
        mycursor.execute("SELECT password FROM Psswd WHERE program='%s'" % (program))
        resul=mycursor.fetchone()
        return resul
