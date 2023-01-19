import multiprocessing
import threading
def threadx1():
    n=0
    while n<=50:
        print("Thread1:",n)
        n=n+1

def threadx2():
    n=50
    while n>0:
        print("Thread2:",n)
        n=n-1

        


def main():

    p1=threading.Thread(target=threadx1,)
    p1.start()
    p1.join()
    p2 = threading.Thread(target=threadx2, )
    p2.start()
    p2.join()


if __name__=="__main__":
    main()