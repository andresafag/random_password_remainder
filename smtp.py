
import smtplib
import os

# SET THE PARAMETERS OF THE  MSG
password = os.environ["PSW"]
sender= "************@gmail.com"
receiver = "***************@gmail.com"

# CREATE A SERVER
def send(passwd, app):
    # CONNECT TO THE SMTP SERVER|
    server = smtplib.SMTP('smtp.gmail.com')
    server.starttls()
    # LOGIN CREDENTIALS FOR SENDING THE MAIL
    server.login(sender, '**********')
    message = "The password is {}  and the app name is {}".format(passwd, app)
    server.sendmail(sender, receiver, message)
    server.quit()
    print("Sent email to %s" % (receiver))
