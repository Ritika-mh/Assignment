def fact(No):

    if (No<=0):
        return 1
    else:
        return (No*fact(No-1))

def main():
    NO=int(input("Enter input:"))
    Ret=fact(NO)
    print("Factorial  is:",Ret)
if __name__=="__main__":
    main()