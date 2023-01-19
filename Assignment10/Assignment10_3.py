import os
from pathlib import Path
from sys import *
import shutil

def Directory_Filecopy(O_Dir,D_Dir):
    print("Inside Directory File copy")
    print("Name of input directory:",O_Dir)
    os.mkdir(D_Dir)
    for Foldername,subfolder,filenames in os.walk(O_Dir):
        for file in filenames:
            shutil.copy2(os.path.join(O_Dir,file),D_Dir)


def main():
    print("Directory File copy application")
    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name File_Extension")
        exit()

    if (len(argv) < 3):
        print("Insufficient arguments")
        exit()
    Directory_Filecopy(argv[1],argv[2])

if(__name__ == "__main__"):
    main()