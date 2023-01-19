#Accept two no and perform addition and substraction
#class==Characteristics+behaviour
#class=Data+function

class Arithmatic:
    def __init__(self,A,B):
        self.No1=A
        self.No2=B
    def Add(self):
        return self.No1+self.No2


    def Sub(self):
        return self.No1-self.No2

def main():
    print("enter first no")
    value1 = int(input())

    print("enter second no")
    value2 = int(input())

    obj=Arithmatic(value1,value2)
    Ans=obj.Add()
    print("Addition is:",Ans)
    Ans=obj.Sub()
    print("Substraction is:",Ans)

if __name__=="__main__":
    main()