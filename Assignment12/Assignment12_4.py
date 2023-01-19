import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import psutil
from datetime import datetime
import time
from sys import *


def ProcessDisplay(Rid,log_dir="Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir, "MarvellousLog%s.log" % (time.time()))
    Filename = log_path
    print(Filename)
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write("Marvellous Infosystem Process Logger:" + time.ctime() + "\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    for element in listprocess:
        f.write("%s\n" % element)
    mailsend(Rid, Filename)


def mailsend(Recever_id, Mattach):
    mail_content = "Hello"
    # The mail addresses and password


    sender_address = 'rhachhad@gmail.com'
    sender_pass = 'jhyvulzxxdscvejq'
    receiver_address = Recever_id
    # Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'
    # The subject line
    # The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    attach_file_name = Mattach
    attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
    payload = MIMEBase('application', 'octate-stream')
    payload.set_payload((attach_file).read())
    encoders.encode_base64(payload)  # encode the attachment
    # add payload header with filename
    payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
    message.attach(payload)
    # Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
    session.starttls()  # enable security
    session.login(sender_address, sender_pass)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')


def main():
    print("_______Marvellous INfosystem_________")

    print("Application name:" + argv[0])

    if (len(argv) != 3):
        print("Error :Invalid number of arguments")
        exit()

    if ((argv[1] == "-h") or (argv[1] == "-H")):
        print("Script is used log records of running process")
        exit()

    if ((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage:ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[2], argv[1])

    except ValueError:
        print("Error:Invalid datatype of input")
     except Exception as E:
       print("Invalid input",E)


if __name__ == "__main__":
    main()
