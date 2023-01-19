import os
import filecmp
from sys import *
def Filesearch(File1,String):
    if os.path.exists(File1):
        fd=open(File1,"r")
        content=fd.read()
        frequency=content.count(String)
        print("frequency of {} is:".format(String),frequency)
    else:
        print("File1 does not exist")
def main():
    
    Filesearch(argv[1],argv[2])

if __name__=="__main__":
    main()