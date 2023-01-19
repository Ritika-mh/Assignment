
def Add_Digits(N):#879
    if N<=0:
        return 0
    else:
        Ans = 0
        a=N%10#(9)
        N//=10#(87)
        Ans +=a
        return (Ans + Add_Digits(N))


def main():

    C=int(input("Enter number"))
    Result=Add_Digits(C)
    print("Addition of Digits is:",Result)


if __name__=="__main__":
    main()