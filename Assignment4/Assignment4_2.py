print("Program to find multiplication of given two input using lambda function")
multi=lambda A,B:B*A
def main():
    A=int(input("enter input1:"))
    B = int(input("enter input2:"))
    Ans=multi(A,B)
    print("output is:",Ans)
if __name__=="__main__":
    main()