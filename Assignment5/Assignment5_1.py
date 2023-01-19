class Bookstore():
    NoofBooks=0
    def __init__(self,String1,String2):
        self.name=""
        self.Auther=""
    def Display(self):
        print(self.name)
        print(self.Auther)
        Bookstore.NoofBooks=Bookstore.NoofBooks+1
        print(Bookstore.NoofBooks)

def main():
    obj1=Bookstore("Linux","Robert love")
    obj1.Display()

    obj2=Bookstore("C","Dennies Ritchie")
    obj2.Display()


if __name__=="__main__":
    main()