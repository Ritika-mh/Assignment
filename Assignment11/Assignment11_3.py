import os
import hashlib
from sys import *

def Directory_Checksumcal(Dir):
    print("Inside Duplicate file searching and deleting Application")
    print("Name of input directory:", Dir)
    listchecksum = []
    Duplicatfile = []
    separator = "-" * 80
    log_path = os.path.join(Dir, "log.log")
    f= open(log_path, 'w')
    f.write(separator+ "\n")

    for Foldername, subfolder, filenames in os.walk(Dir):
        for file in filenames:
            file1 = os.path.join(Foldername, file)
            if os.path.exists(file1):
                fd = open(file1, "r")
                Data = fd.read()
                fd.close()
                readable_hash = hashlib.md5(Data.encode('utf-8')).hexdigest()
                if readable_hash not in listchecksum:
                    listchecksum.append(readable_hash)
                else:
                    Duplicatfile.append(file1)
                    print(Duplicatfile)


    for element in Duplicatfile:
        f.write("%s\n" % element)
        os.remove(element)

def main():
    print("Python Automation")
    if (argv[1] == "-h"):
        print("This script will travel the directory and write name of duplicate file in directory and delet them")
        exit()

    if (argv[1] == "-u"):
        print("Usage : Application_name and Direcory_Name and File log name ")
        exit()

    if (len(argv) < 2):
        print("Insufficient arguments")
        exit()

    Directory_Checksumcal(argv[1])


if (__name__  == "__main__"):
    main()