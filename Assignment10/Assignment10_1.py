import os
from sys import *

def Directory_Filesearch(Dir_Name,Fileextension):
    print("Inside Directory File search")
    print("Name of input directory:",Dir_Name)

    for Foldername,subfolder,filenames in os.walk(Dir_Name):
        for file in filenames:
            if file.lower().endswith(Fileextension):
                print(file)
                print("")
def main():
    print("Directory File search application")


    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name File_Extension")
        exit()
    if (len(argv) < 3):
        print("Insufficient arguments")
        exit()

    Directory_Filesearch(argv[1],argv[2])

if(__name__ == "__main__"):
    main()