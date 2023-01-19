class Numbers:
    def __init__(self):
        print("enter number:")
        self.value=int(input())

    def Checkprime(self):
        i=0
        Flag=True
        for i in range(2,int(self.value/2)+1):
            if (self.value%i)==0:
                Flag=False
                break
        return Flag
    def Sumfactors(self):
        Sum=0
        for i in range(1, int(self.value / 2) + 1):
            if (self.value % i) == 0:
                Sum=Sum+i
        return Sum
    def Checkperfect(self):
        Ans=self.Sumfactors()
        if self.value==Ans:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are:")
        for i in range(1, int(self.value / 2) + 1):
            if (self.value % i) == 0:
                print(i)


def main():
    NO1=Numbers()
    output=NO1.Checkprime()
    print("output is:",output)
    output=NO1.Sumfactors()
    print("Sum of factors of no is:",output)
    output=NO1.Checkperfect()
    print("output is:",output)
    NO1.Factors()

if __name__=="__main__":
    main()