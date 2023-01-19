import multiprocessing
import threading

def DisplayEven():
    i = 1
    n = 0
    while (n < 10):
        if i % 2 == 0:
            print("Even no:",i)
            i = i + 1
            n = n + 1
        else:
            i = i + 1
def DisplayOdd():
    i = 1
    n = 0
    while (n < 10):
        if i % 2 != 0:
            print("Odd no:",i)
            i = i + 1
            n = n + 1
        else:
            i = i + 1
def main():
    print("Demonstration of Parellel programming using multiple Threads")


    p1 = threading.Thread(target=DisplayEven)
    p2 = threading.Thread(target=DisplayOdd)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
    
if __name__=="__main__":

    main()
