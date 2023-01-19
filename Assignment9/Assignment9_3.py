import os
import shutil
from sys import *
def Filesearch(Filename):
    if os.path.exists(Filename):
        fd=open(Filename,"r")
        fd=open("Demo.txt","w")
        shutil.copyfile(Filename,"Demo.txt")

    else:
        print("File does not exist")
def main():
    
    Filesearch(argv[1])

if __name__=="__main__":
    main()