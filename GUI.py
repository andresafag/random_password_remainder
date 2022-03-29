import tkinter as tk
# IMPORT THE RANDOM PASSWORD ALREADY SETUP
from passwd import *
# from notifier import *
# IMPORT THE DATABASE TO 1 MAKE SURE IT IS CONNECTED AND 2 TO SEND THE VALUES DESIRED
from dbs import *
# IMPORT SMTP TO SEND EMAIL NOTIFICATION
from smtp import send
from tkinter import messagebox
import random
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
    if does_exist(entry_name_value) == 0:
        # CALL THE FUNCTION FROM PASSWD.PY AND PROCESS THE PASSWORD AND APP ENTRIES TO SAVE THEM
        password_generated=generate_random_password(entry_passwd_value, entry_name_value)
        if password_generated != None:
            with open('text_passwd.txt', 'a') as reader:
                reader.write("Password generated: " + password_generated + " and " + " app: " + entry_name_value + " \n")
                reader.close()
            print('Done saving in prueba.txt!!')
            # CALLING THE FUNCTION FROM DBS TO SAVE THE INFO IN THE DATABASE
            propasswd(entry_name_value, password_generated)
            print("Everything went through successfully master Andrés")
            # FUNCTION CALLED TO SEND PASSWORD THROUGH EMAIL
            send(password_generated, entry_name_value)
            entry_passwd_value = ""
            entry_name_value = ""
    else:
        messagebox.showwarning(message="Already exists", title="You just entered an existing program")

# BUTTON TO CALL GET VALUE() FUNCTION
btn_send=tk.Button(ventana, text="Create random password", command=get_value)
btn_send.pack()



retrive_msg_frm=tk.LabelFrame(ventana, text="Info retrieval")
retrive_msg_frm.pack(ipadx=50, ipady=100)
retrive_msg_options=tk.Label(retrive_msg_frm, text="What password would you like to retrive")
retrive_msg_options.pack()


program_retrieval_entry=tk.Entry(retrive_msg_frm)
program_retrieval_entry.pack()


passwd_show=tk.Label(retrive_msg_frm, text="")
passwd_show.pack()


def retrieve_passwd():
    try:
        program_value_to_retrieve=program_retrieval_entry.get()
        print(program_value_to_retrieve)
        program_passwd=search_program(program_value_to_retrieve)
        print(program_passwd)
        if program_passwd != None:
            passwd_show["text"]="{}".format(program_passwd)
        elif program_passwd == None:
            passwd_show["text"]="That value does not exit...Try again"
    except:
        print("error")


passwd_retrieval_onclick=tk.Button(retrive_msg_frm, text="Retrieve the password", command=retrieve_passwd)
passwd_retrieval_onclick.pack()




ventana.mainloop()
