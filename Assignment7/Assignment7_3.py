import multiprocessing
import threading


def Evenlist(Data):
    Add = 0
    for No in Data:
        if (No % 2 == 0):
                Add=Add+No
    print("Addition of Even no in list is:",Add)


def Oddlist(Data):
    Add = 0
    for No in Data:
        if (No % 2 != 0):
            Add = Add + No
    print("Addition of Odd no in list is:", Add)

def main():
    print("enter no of elements")
    i = int(input())
    Arr = []
    print("enter numbers")
    for a in range(i):
        m = int(input())
        Arr.append(m)
    print("Input list is:", Arr)

    p1 = threading.Thread(target=Evenlist, args=(Arr,))
    p2 = threading.Thread(target=Oddlist, args=(Arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()