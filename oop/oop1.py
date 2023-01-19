
class Arithmatic:
    def __init__(self,A,B):
        self.no1=A
        self.no2=B

    def Addition(self):
        Ans=self.no1+self.no2
        return Ans

    def substraction(self):
        Ans = self.no1 - self.no2
        return Ans


def main():
    print("Inside main method")

    obj=Arithmatic(11,10)
    output=obj.Addition()
    print("Addition is:",output)
    output = obj.substraction()
    print("Substraction  is:",output)
if __name__=="__main__":
    print("Inside starter")
    main()