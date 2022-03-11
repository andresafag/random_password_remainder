import tkinter as tk
# IMPORT THE RANDOM PASSWORD ALREADY SETUP
from passwd import *
# IMPORT THE DATABASE TO 1 MAKE SURE IT IS CONNECTED AND 2 TO SEND THE VALUES DESIRED
from dbs import *
# IMPORT SMTP TO SEND EMAIL NOTIFICATION
from smtp import send

# CONNECT TO MYSQL DB
connect_sql

# Show DATABASES
# GetDbs()

# MAIN GUI WINDOWS CONTAINER
ventana = tk.Tk()
ventana.geometry("850x400")

# INSTRUCTIONS FOR THE USER
instrct_label=tk.Label(ventana, text="Type in name of the program and the length of the password...longer than 6 digits").pack(side = tk.TOP)

# ENTRY THE APP NAME
name_entry=tk.Entry(ventana)
name_entry.pack(anchor=tk.CENTER)

# ENTRY THE PASSWORD LENGTH
entry_passwd=tk.Entry(ventana)
entry_passwd.pack(anchor=tk.CENTER)
entry_passwd.insert(0, "Enter the password")

# FUNCTION TO CALL ONCE CLICKED TO GET THE INFO PROCESSED AND SAVED
def get_value():
    # GET PASSWORD VALUE LENGTH
    entry_passwd_value=entry_passwd.get()
    # GET APP VALUE STRING
    entry_name_value=name_entry.get()
    # CALL THE FUNCTION FROM PASSWD.PY AND PROCESS THE PASSWORD AND APP ENTRIES TO SAVE THEM
    password_generated=generate_random_password(entry_passwd_value)
    if password_generated != None:
        with open('text_passwd.txt', 'a') as reader:
            reader.write("Password generated: " + password_generated + " and " + " app: " + entry_name_value + " \n")
            reader.close()
        print('Done saving in prueba.txt!!')
        # CALLING THE FUNCTION FROM DBS TO SAVE THE INFO IN THE DATABASE
        propasswd(entry_name_value, password_generated)
        print("Everything went through successfully master Andrés")
        # FUNCTION CALLED TO SEND PASSWORD THROUGH EMAIL
        send(password_generated, entry_passwd_value)
    else:
        print("Less than 6")



# BUTTON TO CALL GET VALUE() FUNCTION
btn_send=tk.Button(ventana, text="CLICK HERE", command=get_value)
btn_send.pack()



ventana.mainloop()
