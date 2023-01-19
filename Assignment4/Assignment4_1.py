print("Program to find power of two of entered input using lambda function")
power=lambda A:A*A
def main():
    A=int(input("enter input"))
    Ans=power(A)
    print("output is:",Ans)
if __name__=="__main__":
    main()