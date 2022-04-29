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
from multiprocessing import Process



# CONNECT TO MYSQL DB
connect_sql

# Show DATABASES
# GetDbs()

# MAIN GUI WINDOWS CONTAINER
ventana = tk.Tk()
ventana['background']='#FFFFCC'
ventana.title="Password retrieval"
ventana.geometry("600x400")

# INSTRUCTIONS FOR THE USER
instrct_label=tk.Label(ventana, text="Type in name of the program and the length of the password...longer than 6 digits", bg='#FFFFCC').pack(side = tk.TOP)


def deleteApp(event):
    print(event)
    name_entry.delete(0, "end")

def deletePsswd(event):
    entry_passwd.delete(0, "end")

# def delete

# ENTRY THE APP NAME
name_entry=tk.Entry(ventana)
name_entry.pack(anchor=tk.CENTER, padx = 10, pady = 10)
name_entry.insert(0, "Enter the ap name")
name_entry.bind('<1>', deleteApp)



# ENTRY THE PASSWORD LENGTH
entry_passwd=tk.Entry(ventana)
entry_passwd.bind('<1>', deletePsswd)
entry_passwd.pack(anchor=tk.CENTER, padx = 10, pady = 10)
entry_passwd.insert(0, "Enter the password")


# FUNCTION TO CALL ONCE CLICKED TO GET THE INFO PROCESSED AND SAVED
def get_value():
    # GET PASSWORD VALUE LENGTH
    entry_passwd_value=entry_passwd.get()
    # GET APP VALUE STRING
    entry_name_value=name_entry.get()
    # IF DB HAS IS 0 MEANS VALUE ALREADY EXISTS COMING FROM DBS
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
            msj=messagebox.showinfo("Done", "Your value has been saved")
            name_entry.delete(0, "end")
            entry_passwd.delete(0, "end")
    else:
        messagebox.showwarning(message="Already exists", title="You just entered an existing program")

# BUTTON TO CALL GET VALUE() FUNCTION
btn_send=tk.Button(ventana, text="Create random password",  bg='#9cf', command=get_value)
btn_send.pack(padx = 5, pady = 5)



retrive_msg_frm=tk.LabelFrame(ventana, text="Info retrieval", bg='#FFE5CC')
retrive_msg_frm.pack(ipadx=50, ipady=100)
retrive_msg_options=tk.Label(retrive_msg_frm, text="What password would you like to retrive", bg='#FFE5CC')
retrive_msg_options.pack(padx = 10, pady = 10)


program_retrieval_entry=tk.Entry(retrive_msg_frm)
program_retrieval_entry.pack()
program_retrieval_entry

passwd_show=tk.Label(retrive_msg_frm, bg='#FFE5CC')
passwd_show.pack()


def retrieve_passwd():
    valor=search_program(program_retrieval_entry.get())
    if valor != None:
        # Execution of search program coming from dbs.py
        print(program_retrieval_entry.get())
        passwd_show['text']=valor
        program_retrieval_entry.delete(0, "end")
    elif valor == None:
        passwd_show['text']="That program is does not the database..."
        program_retrieval_entry.delete(0, "end")




passwd_retrieval_onclick=tk.Button(retrive_msg_frm, text="Retrieve the password", command=retrieve_passwd, bg='#9Cf')
passwd_retrieval_onclick.pack(pady=15)
passwd_retrieval_onclick.bind('<Key>', retrieve_passwd)



ventana.mainloop()
