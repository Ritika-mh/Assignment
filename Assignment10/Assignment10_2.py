import os
from sys import *

def Directory_Filerename(Dir_Name,oldFileextension,newfileextension):
    print("Inside Directory File rename")
    print("Name of input directory:",Dir_Name)

    for Foldername,subfolder,filenames in os.walk(Dir_Name):
        for file in filenames:
            if file.endswith(oldFileextension):
                print("Before rename:",file)
                print("")
                old_file_name=os.path.join(Foldername, file)
                new_file_name=old_file_name.replace(oldFileextension,newfileextension)
                file1=os.rename(old_file_name,new_file_name)
                print("After rename:",new_file_name)
def main():
    print("Directory File rename application")

    

    if(argv[1] == "-h"):
        print("This script will travel the directory and display the names of all entries")
        exit()

    if(argv[1] == "-u"):
        print("Usage : Application_name Direcory_Name File_Extension")
        exit()
    if (len(argv) < 4):
        print("Insufficient arguments")
        exit()
    Directory_Filerename(argv[1],argv[2],argv[3])

if(__name__ == "__main__"):
    main()