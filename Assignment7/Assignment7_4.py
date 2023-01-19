import multiprocessing
import threading

def small(Name):
    S=0
    for i in Name:
        if (i>='a' and i<='z'):
            S=S+1
    print("Addition of no of Small latters is",S)

def capital(Name):
    L=0
    for i in Name:
        if (i>='A' and i<='Z'):
            L=L+1
    print("Addition of no of large latters is",L)

def Digit(Name):
    D=0
    for i in Name:
        if i.isnumeric():
            D = D + 1
    print("Addition of no og digits is:",D)

def main():
    print("Enter paramer(strinf or digit)")
    Name=input()

    p1=threading.Thread(target=small,args=(Name,))
    p2=threading.Thread(target=capital, args=(Name,))
    p3=threading.Thread(target=Digit, args=(Name,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("Completed the process")

if __name__=="__main__":
    main()