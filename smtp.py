
import smtplib
import os

# SET THE PARAMETERS OF THE  MSG
password = os.environ["PSW"]
sender= "sampleemail@gmail.com"
receiver = "sampleemail@gmail.com"

# CREATE A SERVER
def send(passwd, app):
    try:
        # CONNECT TO THE SMTP SERVER|
        server = smtplib.SMTP('smtp.gmail.com')
        server.starttls()
        # LOGIN CREDENTIALS FOR SENDING THE MAIL
        server.login(sender, '************')
        message = "The password is %s  and the app name is %s" % (passwd, app)
        server.sendmail(sender, receiver, message)
        server.quit()
        print("Sent email to %s" % (receiver))
    except smtplib.SMTPAuthenticationError as er:
        print("Ooops this is the error {}".format(er))
