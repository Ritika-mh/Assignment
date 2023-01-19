import os
import psutil
from datetime import datetime
import  time
from sys import *

def ProcessDisplay(log_dir):
    listprocess=[]

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator="-"*80
    log_path=os.path.join(log_dir,"MarvellousLog%s.log" %(time.time()))
    f=open(log_path,'w')
    f.write(separator+"\n")
    f.write("Marvellous Infosystem Process Logger:"+time.ctime()+"\n")
    f.write(separator+ "\n")

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass


    for element in listprocess:
        f.write("%s\n" % element)
def main():
    print("_______Marvellous INfosystem_________")

    print("Application name:" +argv[0])

    if (len(argv)!=2):
        print("Error :Invalid number of arguments")
        exit()

    if ((argv[1]=="-h") or (argv[1]=="-H")):
        print("Script is used log records of running process and save in log file")
        exit()

    if ((argv[1]=="-u") or(argv[1]=="-U")):
        print("Usage:ApplicationName AbsolutePath_of_Directory")
        exit()

    try:
        ProcessDisplay(argv[1])
    except ValueError:
        print("Error:Invalid datatype of input")
    except Exception:
        print("Invalid input")
    

if __name__=="__main__":
    main()
