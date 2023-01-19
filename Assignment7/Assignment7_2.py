import multiprocessing
import threading


def Evenfactor(No):
    Add=0
    for i in range(1, No, 1):
        if (No%i==0):
            if (i % 2 == 0):

                Add=Add+i
    print("Addition of Evenfactor is:",Add)


def Oddfactor(No):
    Add = 0
    for i in range(1, No, 1):
        if (No % i == 0):
            if (i % 2 != 0):
                Add = Add + i
    print("Addition of Oddfactor is:", Add)

def main():

    Number =int(input("Enter number"))

    p1 = threading.Thread(target=Evenfactor, args=(Number,))
    p2 = threading.Thread(target=Oddfactor, args=(Number,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()