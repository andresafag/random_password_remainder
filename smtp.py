sender = "danielgarciaacosta46@gmail.com"
receiver = ["brigethedith01@gmail.com"]

message = """From: From Person <danielgarciaacosta46@gmail.com>
To: To Person <brigethedith01@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""


try:
    import smtplib
    server = smtplib.SMTP('localhost')
    server.login('')
    # server.log('danielgarciaacosta46@gmail.com', 'Ironman.12')
    # print("connected")
    # smtpObj.sendmail(sender, receiver, message)
    print("Sent email")
except:
   print("Error: unable to send email")
