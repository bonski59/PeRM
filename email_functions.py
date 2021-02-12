# this module focuses on using outlook/gmail(for testing) to build email attachments with required content and send them to the required recipients

import os.path
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(email_recipient,
               email_subject,
               email_message,
               attachment_location=''):
    email_sender = 'charliekil0159@gmail.com'

    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_recipient
    msg['Subject'] = email_subject

    msg.attach(MIMEText(email_message, 'plain'))

    if attachment_location != '':
        filename = os.path.basename(attachment_location)
        attachment = open(attachment_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= %s" % filename)
        msg.attach(part)


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('charliekil0159@gmail.com', 'ck1590!@')
    text = msg.as_string()
    server.sendmail(email_sender, email_recipient, text)
    server.quit()


    return


send_email('blake.ufp@gmail.com',
           'Example Email',
           'I sent this with python.... this is a burner account', '')








"""import smtplib
import email.utils
from email.mime.text import MIMEText

# Create the message
msg = MIMEText('This is the body of the message.')
msg['To'] = email.utils.formataddr(('Recipient', 'corbinkelly15@gmail.com'))
msg['From'] = email.utils.formataddr(('Author', 'corbinkelly15@gmail.com'))
msg['Subject'] = 'Simple test message'

server = smtplib.SMTP('127.0.0.1', 1025)
server.set_debuglevel(True) # show communication with the server
try:
    server.sendmail('corbinkelly15@gmail.com', ['corbinkelly15@gmail.com'], msg.as_string())
finally:
    server.quit()
"""

"""import os
import smtplib  # Import smtplib for the actual sending function
from email.message import EmailMessage  # Import the email modules we'll need

textfile = r"{}\testemail.txt".format(os.getcwd())

# Open the plain text file whose name is in textfile for reading.
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = "corbinkelly15@gmail.com"
msg['To'] = "blake.ufp@gmail.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()"""
