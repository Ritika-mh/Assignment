print("Program to find minimum(smallest)number in  list")

def Minn(Data):
    Ans = 0
    min=Data[0]
    for j in range(len(Data)-1):

        N1=Data[j]

        if N1<min:
            min=N1
        
    Ans=min
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
    Ans=Minn(Arr)
    print("smallest no is:",Ans)


if __name__=="__main__":
    main()