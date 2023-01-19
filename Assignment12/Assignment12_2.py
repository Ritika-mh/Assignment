import psutil
from sys import *

def ProcessDisplay(pname):

    listProcess=[]

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            if proc.name() == pname:
                listProcess.append(pinfo)
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listProcess
def main():
    print("Marvellous Infosystem")
    print("Process Monitor with memmory usage")
    listprocess=ProcessDisplay(argv[1])
    for elem in listprocess:
        print(elem)
if __name__=="__main__":
    main()