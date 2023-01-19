class Circle:
    PI=3.14
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self):
        print("Enter value of Radius:")
        self.Radius=float(input())

    def CalculateArea(self):
        self.Area= self.Radius*self.Radius * Circle.PI
    def Calculatecircumference(self):
        self.Circumference=2*( Circle.PI) *self.Radius
        
    def Display(self):
        print("Area of circle is:",self.Area)
        print("Circumference of cicle is:",self.Circumference)



def main():
    print("value of PI is:",Circle.PI)
    obj = Circle()
    obj.Accept()
    obj.CalculateArea()
    obj.Calculatecircumference()
    obj.Display()
    
if __name__=="__main__":
    main()

