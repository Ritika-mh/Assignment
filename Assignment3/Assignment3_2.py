print("Program to find largest number in list")
#1 3 6 7 4
def Maxn(Data):
    Ans = 0
    max=Data[0]
    for j in range(len(Data)-1):

        N1=Data[j]

        if N1>max:
            max=N1
        
    Ans=max
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
    Ans=Maxn(Arr)
    print("largest no is:",Ans)


if __name__=="__main__":
    main()