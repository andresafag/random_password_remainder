import tkinter as tk
from passwd import *
from dbs import *

# connect_mysql()
myPasswds

# Show DATABASES
# GetDbs()




#   window where all elements will live in
ventana = tk.Tk()
ventana.geometry("850x400")

# instructions for the user
instrct_label=tk.Label(ventana, text="Type in name of the program and the length of the password...longer than 6 digits").pack(side = tk.TOP)

# entry for app name
name_entry=tk.Entry(ventana)
name_entry.pack(anchor=tk.CENTER)

# Entry for password
entry_passwd=tk.Entry(ventana)
entry_passwd.pack(anchor=tk.CENTER)
entry_passwd.insert(0, "Enter the password")

def get_value():
    # Get entry_passwd value
    entry_passwd_value=entry_passwd.get()
    # Get entry for name
    entry_name_value=name_entry.get()
    # save the random password generator in password_generated
    password_generated=generate_random_password(entry_passwd_value)
    if password_generated != None:
        with open('prueba.txt', 'a') as reader:
            reader.write("Contraseña generada: " + password_generated + " y " + " Aplicación: " + entry_name_value + " \n")
            reader.close()
        print('Done saving in prueba.txt!!')
        propasswd(entry_name_value, password_generated)
        print("Everything went through successfully master Andrés")
    else:
        print("Less than 6")

btn_send=tk.Button(ventana, text="CLICK HERE", command=get_value)
btn_send.pack()


ventana.mainloop()
