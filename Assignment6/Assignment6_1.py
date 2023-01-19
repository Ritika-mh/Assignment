class BookStore:
    NoofBook=0
    def __init__(self,N,A):
        self.Name=N
        self.Author=A

    def Display(self):
        BookStore.NoofBook +=1
        print("{} by {} . No of books: {}".format(self.Name,self.Author,BookStore.NoofBook))



def main():
    Book1=BookStore("Linux System Programming","Robert Love")
    Book1.Display()

    Book2 = BookStore("C Programming", "Dennis Ritchie")
    Book2.Display()


if __name__=="__main__":
    main()