print("Program to find prime number and creat list of it and add all prime number's in the list")
import MarvellousNum
def ListPrime(Data):
    prime=[]    
    for n in Data:
        Ansp = MarvellousNum.Checkprime(n)


        prime.append(Ansp)
    return prime

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

    prime=ListPrime(Arr)
    print("List of prime no is:",prime)

    Ans=Add(prime)
    print("Addition of prime no is",Ans)



if __name__=="__main__":
    main()