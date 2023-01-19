import os
import filecmp
from sys import *
def Filesearch(File1,File2):
    if os.path.exists(File1):
        fd=open(File1,"r")
        if os.path.exists(File2):
            fd=open(File2,"r")
            Result=filecmp.cmp(File1,File2,shallow=False)
            if Result == True:
                print("Success")
            else:
                print("Failure")
        else:
            print("File2 does not exist")
    else:
        print("File1 does not exist")
def main():
    
    Filesearch(argv[1],argv[2])

if __name__=="__main__":
    main()