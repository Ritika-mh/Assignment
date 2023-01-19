import os
from sys import *

def Directory_Watcher(Dir_Name):
    print("Inside Directory watcher")
    print("Nmae of input directory:",Dir_Name)

    for Foldername,subfolder,filenames in os.walk(Dir_Name):
        print("folder name is:"+Foldername)
        for subf in subfolder:
            print("Subfoldef name of "+Foldername+"is "+subf)
            for fnames in filenames:
                print("File inside folder "+Foldername+" is "+fnames)
            print("")
def main():
    print("Directory watcher application")

    if(len(argv) < 2):
        print("Insufficient arguments")
        exit()

    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name")
        exit()

    Directory_Watcher(argv[1])

if(__name__ == "__main__"):
    main()