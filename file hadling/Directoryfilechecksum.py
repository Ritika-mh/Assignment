import os
import hashlib
from sys import *
def hashfile(path,blocksize=1024):
    afile=open(path,"rb")
    hasher=hashlib.md5()
    buf=afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def Directory_Checksumcal(path):
    flag=os.path.isabs(path)
    if flag== False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)

    if exists:
        for Dirname,subdi,filelist in os.walk(path):
            print("current folder is:" +Dirname)
            for flen in filelist:
                path=os.path.join(Dirname,flen)
                file_hash=hashfile(path)
                print(file_hash)
       

    else:
        print("Invalid Path")
        exit()

def main():
    print("Directory Checksum cal  application")
    if(argv[1] == "-h")  or(argv[1]=="-H"):
        print("This script will travel the directory and display checksum of files")
        exit()

    if(argv[1] == "-u") or (argv[1]=="-U"):
        print("Usage : Application_name Direcory_Name ")
        exit()

    if (len(argv) != 2):
        print("Insufficient arguments")
        exit()
    try:
        arr=Directory_Checksumcal(argv[1])
    except ValueError:
        print("Error:Invalid datatype of input")
    except Exception as E:
        print("Error:Invalid input",E)

if(__name__ == "__main__"):
    main()