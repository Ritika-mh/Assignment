import os
import hashlib
from sys import *
import time

def hashfile(path,blocksize=1024):
    afile=open(path,"rb")
    hasher=hashlib.md5()
    buf=afile.read(blocksize)
    while len(buf)>0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def FindDuplicate(path):
    flag=os.path.isabs(path)
    if flag== False:
        path=os.path.abspath(path)

    exists=os.path.isdir(path)
    dups={}
    if exists:
        for Dirname,subdi,filelist in os.walk(path):
            for flen in filelist:
                path=os.path.join(Dirname,flen)
                file_hash=hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash]=[path]

        return dups
    else:
        print("Invalid Path")
        exit()
def Deletefiles(dict1):
    results=list(filter(lambda x:len(x)>1,dict1.values()))
    icnt = 0
    if len(results)>0:
        for result in results:
            for subresult in result:
                icnt+=1
                if icnt>=2:
                    os.remove(subresult)
            icnt=0
    
def logentry(dict1,Dir):
    separator = "-" * 80
    log_path = os.path.join(Dir, "log.log")
    f = open(log_path, 'w')
    f.write(separator + "\n")

    results=list(filter(lambda x:len(x)>1,dict1.values()))
    if len(results)>0:

        for result in results:
            for subresult in result:
                print('\t\t%s' %subresult)
                f.write("%s\n" % subresult)

    else:
        Data='No duplicate files found.'
        f.write( Data)


def main():
    print("Directory Checksum cal  application")
    print("Application name:",argv[0])
    if(argv[1] == "-h")  or(argv[1]=="-H"):
        print("This script will travel the directory and delet duplicate files")
        exit()

    if(argv[1] == "-u") or (argv[1]=="-U"):
        print("Usage : Application_name Direcory_Name ")
        exit()

    if (len(argv) != 2):
        print("Insufficient arguments")
        exit()
    try:
        arr={ }
        startTime=time.time()
        arr=FindDuplicate(argv[1])
        logentry(arr,argv[1])
        Deletefiles(arr)
        endtime=time.time()
        print('Tool %s seconds to evaluate.'%(endtime-startTime))
    except ValueError:
        print("Error:Invalid datatype of input")
    except Exception as E:
        print("Error:Invalid input",E)

if(__name__ == "__main__"):
    main()