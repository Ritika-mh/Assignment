import os
import hashlib
from sys import *


def Directory_Checksumcal(Dir):
    print("Inside Directory Checksum cal")
    print("Name of input directory:",Dir)

    for Foldername,subfolder,filenames in os.walk(Dir):
        for file in filenames:
            file1=os.path.join(Foldername, file)
            if os.path.exists(file1):
                fd = open(file1, "r")
                Data = fd.read()
                readable_hash = hashlib.md5(Data.encode('utf-8')).hexdigest()
                print(readable_hash)

def main():
    print("Directory Checksum cal  application")
    if(argv[1] == "-h"):
        print("This script will travel the directory and display checksum of files")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name ")
        exit()

    if (len(argv) < 2):
        print("Insufficient arguments")
        exit()
    Directory_Checksumcal(argv[1])

if(__name__ == "__main__"):
    main()