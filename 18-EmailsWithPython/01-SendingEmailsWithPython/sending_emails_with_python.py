import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()

email = getpass.getpass("What is your Email Address: ")
password = getpass.getpass("What is your Password: ")

smtp_object.login(email, password)

from_address = email
to_address = email
subject = input("Please enter the subject line: ")
message = input("Please enter the body message: ")
msg = "Subject: " + subject + "\n" + message

smtp_object.send_message(from_address, to_address, msg)

smtp_object.quit()