class Arithmatic:
    def __init__(self,A,B):
        self.value1=A
        self.value2=B

    def Addition(self):
        Result=self.value1+self.value2
        return Result
    def Substraction(self):
        Result=self.value1-self.value2
        return Result
    def Multiplication(self):
        Result=self.value1*self.value2
        return Result
    def Division(self):
        Result=self.value1/self.value2
        return Result




def main():
    obj1=Arithmatic(11,10)
    Ans=obj1.Addition()
    print("Addition is:",Ans)
    Ans=obj1.Substraction()
    print("Substraction is:", Ans)
    Ans=obj1.Multiplication()
    print("Multiplication:", Ans)
    Ans=obj1.Division()
    print("Division is:", Ans)

    obj2 = Arithmatic(110, 100)
    Ans = obj2.Addition()
    print("Addition is:", Ans)
    Ans = obj2.Substraction()
    print("Substraction is:", Ans)
    Ans = obj2.Multiplication()
    print("Multiplication:", Ans)
    Ans = obj2.Division()
    print("Division is:", Ans)


if __name__=="__main__":
    main()