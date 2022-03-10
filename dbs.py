import mysql.connector

myPasswds = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ironman.12",
    database="PassWords"
)

print("connected to mysql successfully brother")

mycursor = myPasswds.cursor()


def GetDbs():
    mycursor.execute("SHOW DATABASES")
    for db in mycursor:
        print(db)

def propasswd(value_1, value_2):
    sql = "INSERT INTO Psswd (program, password) VALUES (%s, %s)"
    val = (value_1, value_2)
    mycursor.execute(sql, val)
    myPasswds.commit()
    print(mycursor.rowcount, "record inserted.")
