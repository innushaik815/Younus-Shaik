import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "#####"  # Enter your address
receiver_email = "#####"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email, receiver_email, message)
######################################################################################
    #here the sender needs to turn of his security button and this to be done on your own risk
    ###################################################################################################
