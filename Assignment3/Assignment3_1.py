print("Program to demonstrate Addition of list")
def Add(Data):
    Ans = 0
    for j in Data:

        Ans=Ans+j
    return Ans

def main():
    print("enter no of elements")
    i=int(input())
    Arr=[]
    print("enter numbers")
    for a in range (i):

        m=int(input())
        Arr.append(m)
    print("list is:",Arr)
    Sum=Add(Arr)
    print("Addition is:",Sum)


if __name__=="__main__":
    main()