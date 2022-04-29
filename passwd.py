import random
import string
import time
from tkinter import messagebox

# characters to generate password from
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password(userInput, program):
    # EMPTY PASSWORD ARRAY
    password=[]
    try:
        # USER INPUTS A NUMBER AS A STR AND CONVERTS IT INTO AN INTEGER
        userInput = int(userInput)
        # PASSWORD LENGTH SHOULD BE LONGER THAN 6
        if not program.isnumeric() and userInput > 6:
            # RANDOMLY CHOSEN PASSWORD
            random.shuffle(characters)
            for character in range(userInput):
                password.append(random.choice(characters))
            response = "".join(password)
            # RETURNING THE PASSWORD LENGTH
            return response
        elif userInput <= 6:
            messagebox.showwarning(message="Enter a number greater than 6", title="Not a string")
            return None
        else:
            messagebox.showwarning(message="You are entering a number instead of a string", title="Not a string")
    except ValueError:
        print("This is not an integer buddy")
        messagebox.showwarning(message="This is not an integer buddy", title="Not an integer")
    except:
        print("Something went wrong")
