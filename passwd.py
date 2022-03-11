import random
import string
import time
from tkinter import messagebox

# characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password(userInput):
    # EMPTY PASSWORD
    password=[]
    try:
        # USER INPUTS A NUMBER AS A STR AND CONVERTS IT INTO AN INTEGER
        userInput = int(userInput)
        # PASSWORD LENGTH SHOULD BE LONGER THAN 6
        if userInput > 6:
            time.sleep(4)
            # RANDOMLY CHOSEN PASSWORD
            random.shuffle(characters)
            for character in range(userInput):
                password.append(random.choice(characters))
            response = "".join(password)
            # RETURNING THE PASSWORD LENGTH
            return response
        elif userInput <= 6:
            return None
    except ValueError:
        print("This is not an integer buddy")
        messagebox.showwarning(message="This is not an integer buddy", title="Not an integer")
























#     if type(userInput) == int:
#         print("It is an integer...wait till we get you a new password")
#         time.sleep(4)
#         random.shuffle(characters)
#         for character in range(userInput):
#             password.append(random.choice(characters))
#         print("".join(password))
#     elif type(userInput) == str:
#         integ=int(userInput)
#         print("It is an integer...wait till we get you a new password")
#         time.sleep(4)
#         random.shuffle(characters)
#         for character in range(integ):
#             password.append(random.choice(characters))
#         print("Almost ready")
#         return "".join(password)
#     else:
#         print("You messed it up")
#
# # generate_random_password()
