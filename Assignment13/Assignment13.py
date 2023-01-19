import os
import hashlib
from sys import *
import time
import schedule
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
def ProcessDuplicate():
    arr = {}
    arr = FindDuplicate(argv[1])
    logentry(arr,argv[3])
    Deletefiles(arr)

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




def hashfile(path, blocksize=1024):
    afile = open(path, "rb")
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def FindDuplicate(path):
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    dups = {}
    if exists:
        for Dirname, subdi, filelist in os.walk(path):
            for flen in filelist:
                path = os.path.join(Dirname, flen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid Path")
        exit()


def Deletefiles(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    icnt = 0
    if len(results) > 0:
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >= 2:
                    os.remove(subresult)
            icnt = 0


def logentry(dict1,Rid,log_dir="Marvellous"):
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    separator = "-" * 80
    log_path= os.path.join(log_dir, "logenrty%s.log" %(time.time()))
    Filename = log_path
    f = open(log_path, 'w')
    f.write(separator + "\n")
    f.write(" Duplicate file deleted entry Log:" + time.ctime() + "\n")

    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:

        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
                f.write("%s\n" % subresult)

    else:
        Data = 'No duplicate files found.'
        f.write(Data)
    mailsend(Rid,Filename )
def shedulerx(timeinm):
    print(timeinm)
    schedule.every(int(timeinm)).minutes.do(ProcessDuplicate)
    while (True):
        schedule.run_pending()
        time.sleep(1)

def main():
    print("Directory Checksum cal  application")
    print("Application name:", argv[0])
    if (argv[1] == "-h") or (argv[1] == "-H"):
        print("This script will travel the directory and delet duplicate files")
        exit()

    if (argv[1] == "-u") or (argv[1] == "-U"):
        print("Usage : Application_name Direcory_Name ")
        exit()

    if (len(argv) != 4):
        print("Insufficient arguments")
        exit()
    try:

        startTime = time.time()
        shedulerx(argv[2])
        endtime = time.time()
        print('Tool %s seconds to evaluate.' % (endtime - startTime))
    except ValueError:
        print("Error:Invalid datatype of input")
     except Exception as E:
     print("Error:Invalid input",E)


if (__name__ == "__main__"):
    main()