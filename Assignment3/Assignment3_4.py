print("Program to find perticular number's frequency in  list")

def freq(Data):
    f=0
    print("enter element to search")
    k = int(input())
    for n in range(len(Data)):
        N1=Data[n]
        if k==N1:
            f=f+1
    return f


def main():
    print("enter no of elements")
    i=int(input())
    Arr=[]
    print("enter numbers")
    for a in range (i):

        m=int(input())
        Arr.append(m)
    print("list is:",Arr)

    Ans=freq(Arr)
    print("output is:",Ans)


if __name__=="__main__":
    main()