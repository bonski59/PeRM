# this module focuses on using outlook/gmail(for testing) to build email attachments with required content and send
# them to the required recipients

import os
import os.path
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd

import folders

email_credentials = {
        'username': 'charliekil0159@gmail.com',  # static variable
        'password': 'ck1590!@',  # static variable
        'sender': 'charliekil0159@gmail.com'
    }



# noinspection PyBroadException
def send_email(email_recipient,
               email_subject,
               email_message,
               attachment_location=''):
    email_sender = email_credentials['username']

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
        server = smtplib.SMTP('smtp.gmail.com', 587)         # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        """make sure this is correct before running"""
        server.ehlo()
        server.starttls()
        server.login(email_credentials['username'], email_credentials['password'])
        text = msg.as_string()
        server.sendmail(email_sender, email_recipient, text)
        server.quit()
    except:
        print("SMPT server connection error")
    return True


def email_everyone():   # explict function that will be referenced in the main.py
    """
    read REPORT_DETAIL.csv
    for every line compose an email
    input variables into a dict inside for loop
    inject variable into "send email" function
    send the email
    """

    # read report
    csv_rep = folders.Paths.reportCSV
    df = pd.read_csv(csv_rep)
    loop_length = int(df.shape[0]) - 1
    # print(df['MAILING_LIST'][0])
    while loop_length >= 0:
        email_content = {'recipients_arr': df['MAILING_LIST'][loop_length], 'subject': df['EMAIL_SUBJECT'][loop_length], 'message': df['EMAIL_BODY'][loop_length], 'attachment_fp_arr': df['Report_Filepath'][loop_length]}
        email_content['message'] = "For Purely Professional Testing Purposes"  # testing
        print(str(email_content))
        send_email(email_content['recipients_arr'], email_content['subject'], email_content['message'], email_content['attachment_fp_arr'])
        loop_length -= 1
    return

email_everyone()










    # example send
"""send_email('corbinkelly15@gmail.com',
           'Excel Email',
           'I sent this with python.... this is a burner account', r'D:\git\PeRM\PeRM\Book1.xlsx')"""
