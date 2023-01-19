class BankAccount:
    ROI=10.5
    def __init__(self):
        print("enter name:")
        self.Name=input()
        self.Amount=0.0
        self.Intrest=0.0
    def Deposit(self):
        print("Enter amount for Deposit")
        value=float(input())
        self.Amount=self.Amount+value

    def Withdraw(self):
        print("Enter amount to withdraw")
        value=float(input())
        self.Amount=self.Amount-value

    def CalculateIntreast(self):
        self.Intrest=(self.Amount*BankAccount.ROI)/100
        

    def Display(self):
        print("name: {} ".format(self.Name))
        print("Amount: {}".format(self.Amount))
        print("Intrest:{}".format(self.Intrest))



def main():
    User1=BankAccount()
    User1.Deposit()
    User1.Withdraw()
    User1.CalculateIntreast()
    User1.Display()

if __name__=="__main__":
    main()