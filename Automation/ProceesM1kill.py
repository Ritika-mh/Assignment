import psutil
import schedule
import time
import datetime

def ProcessDisplay():
    listProcess=[]

    for proc in psutil.process_iter():
        try:
            pinfo=proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms']=proc.memory_info().vms/(1024*1024)

            listProcess.append(pinfo)
            if proc.name() == "notepad.exe":
                proc.kill()
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listProcess
def sheduleprocess():
    schedule.every(10).minutes.do(ProcessDisplay)
    while (True):
        schedule.run_pending()
        time.sleep(1)


def main():
    print("Marvellous Infosystem")
    print("Process Monitor with memmory usage")
    listprocess=ProcessDisplay()
    for elem in listprocess:
        print(elem)
    sheduleprocess()
if __name__=="__main__":
    main()