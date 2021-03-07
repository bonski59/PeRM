# this module focuses on using outlook/gmail(for testing) to build email attachments with required content and send
# them to the required recipients
import os
import os.path
import smtplib
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
import folders
from admin import *

""" email credentials will need to be changed """
if folders.Paths.testing:
    email_credentials = {
        'username': 'charliekil0159@gmail.com',
        'password': 'ck1590!@',
        'sender': 'charliekil0159@gmail.com',
        'smtp_server': 'smtp.gmail.com',
        'smtp_port': 587
    }
else:
    # blake's credentials for dummy account
    # maybe make a csv with this info so that it can be edited by an Access form?
    email_credentials = {
            'username': 'autonotification.ufpi@gmail.com',
            'password': 'as;dlfkj28dLDF',
            'sender': 'autonotification.ufpi@gmail.com',
            'smtp_server': 'smtp.gmail.com',
            'smtp_port': 587
        }

"""
Bread and Butter email function
This will be used in the later loop when iterating through REPORT_DETAILS.csv 

sends single attachment 
uses single sender 
multiple recipients 
subject and message are simple strings 

    I'll be honest, a lot of how this function is built is foreign to me 
    therefore any troubleshooting/changes will have to be done in a debugging capacity separate of 
    important files and or important email login credentials. I can't explain why but I would feel 
    safer doing it that way.  
        -CK
"""


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



    server = smtplib.SMTP(email_credentials['smtp_server'], email_credentials['smtp_port'])
    server.ehlo()
    server.starttls()
    server.login(email_credentials['username'], email_credentials['password'])
    text = msg.as_string()
    #server.send_message(MIMEText(text), email_sender, email_recipient) # changed from sendmail
    server.sendmail(email_sender, email_recipient, text)  # changed from sendmail
    server.quit()

    return True


def email_everyone():                   # explict function that will be imported to main.py
    """
    read REPORT_DETAIL.csv
    for every line compose an email
    TODO: Build QA function before send_email and catch bad info for admin_report
            # does csv content exist i.e.(message, subject, recipient, sender, etc)
            # if false data: admin_report(bad_data) "the following was flagged as bad data"
            # if true data: send_email
            TODO: find out what bad_data qualifies to reroute to admin
    input variables into a dict inside for loop
    inject variable into "send email" function
    send the email
    """

    csv_rep = folders.Paths.reportCSV   # 1: read report, report file must be a static location, otherwise we will need to inject a function property at its definition
    df = pd.read_csv(csv_rep)           # makes pandas dataframe out of csv
    loop_length = int(df.shape[0]) - 1  # calculates loop length by number of lines in csv
    while loop_length >= 0:             # 2: Build loop
        if not df['Verification_Status'][loop_length] or df['REPORT_STATUS'][loop_length] != 'ACTIVE':
            admin_print("**  {}  -- NOT VERIFIED OR NOT ACTIVE --  f/p: {}  **".format(df['REPORT_NAME'][loop_length], df['Report_Filepath'][loop_length]))
            loop_length -= 1
            pass
        else:

            if folders.Paths.testing:       # testing safety net, check folders.py if not testing and confirm class variable
                                             # compose dict for functional reference later
                email_content = {'recipients_arr': df['MAILING_LIST'][loop_length], 'subject': df['EMAIL_SUBJECT'][loop_length],
                                 'message': "For Purely Professional Testing Purposes",
                                 'attachment_fp_arr': df['Report_Filepath'][loop_length]}
            else:
                                            # compose dict for functional reference later
                email_content = {'recipients_arr': "Blake.Kelly.evo@gmail.com",  #  change to df['MAILING_LIST'][loop_length] when live - "blake.ufp@gmail.com,corbinkelly15@gmail.com"
                                 'subject': str(df['EMAIL_SUBJECT'][loop_length]),
                                 'message': str(df['EMAIL_BODY'][loop_length]),
                                 'attachment_fp_arr': df['Report_Filepath'][loop_length]}


            if email_content['message'] == 'nan':
                email_content['message'] = 'This is an Automatic Notification from the UFPI Analyst Team'

            rx_list = email_content['recipients_arr'].split(',')
            admin_print("SENDING : " +  email_content['subject'])
            admin_print("RECIPIENTS: {}".format(rx_list))

            for i in rx_list:
                send_email(i,
                           email_content['subject'],
                           email_content['message'],
                           r"{}\{}".format(folders.Paths.reports_xlsx, email_content['attachment_fp_arr']))


            admin_print("\n SENT \n {} \n {} \n {} \n {}".format(email_content['recipients_arr'], email_content['subject'], email_content['message'], email_content['attachment_fp_arr']))
            loop_length -= 1                # subtract iterable "loop_length" so that the "while" loop will end
    return                              # exit function

def admin_report():
    """
    collect positive and negative data from REPORT_DETAILS.csv
    send info to admin account
    """
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    adm_rep = r"{}\admin_report.txt".format(os.getcwd())
    admin_email = email_credentials['username']
    send_email(admin_email,
               "PeRM: ADMIN REPORT {}".format(now),
               "See Attached",
               adm_rep)
    return

