import smtplib
import ssl

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "hellodk01@gmail.com"
receiver_email = "hello.dk@outlook.com"
password = "113189201@Google"  # input("Type your password")
message = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
