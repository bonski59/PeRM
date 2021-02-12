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

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('charliekil0159@gmail.com', 'ck1590!@')
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        server.quit()
    except:
        print("SMPT server connection error")
    return True



send_email('blake.ufp@gmail.com',
           'Example Email',
           'I sent this with python.... this is a burner account', '')




# reccomend sending confirmation email, i.e. adding your work email into the "TO:" line so you can see it on your phone if needed.

# TODO: make email messaging time based
# TODO: make email messaging execution based (send email to burner account, upon rx burner calls PeRM and emails explicit or implicit target
