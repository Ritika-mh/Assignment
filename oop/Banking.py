
#Instant variable:name,Amount,Address,Acc no
#instanc method:creatacoount()
#class variable:Bank name ,ROI_On_FD
#class method:Display banking information
#static method:DisplayKYCInfo
class Bank_Account:
    Bank_Name="HDFC bank PVT LTD"
    ROI_On_FD=6.7

    def __init__(self):
        self.Name=" "
        self.Amount=0
        self.Address=""
        self.AccountNo=0

    def CreateAccount(self):
        print("enter your name:")
        self.Name=input()

        print("enter your initial amount:")
        self.Amount = int(input())

        print("enter your Address:")
        self.Address = input()

        print("enter your Account no:")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("_____Your Account Information is as below______")
        print("Name of Account holder",self.Name)
        print("Account Number",self.AccountNo)
        print("Address of Account holder",self.Address)
        print("current amount in  Account ",self.Amount)

    @classmethod
    def DisplayBankinformation(cls):
        print("Wlcome to banking console")
        print("Nmae of bank is",cls.Bank_Name)
        print("Rate of intrest on Fixed deposit:",cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below kyc info")
        print("Accordinf to Govr of India submit below document ")
        print("1:clear and recent photo")
        print("2:photo of aadhar card")
        print("3: photo of PAN card")

    def Deposit(self):
        print("enter the amount you want to deposit ")
        value=int(input())
        self.Amount=self.Amount+value

    def Withdraw(self):
        print("enter the amount you want to withdraw ")
        value = int(input())
        self.Amount=self.Amount-value
def main():
    Bank_Account.DisplayKYCInfo()
    print("Name of bank:",Bank_Account.Bank_Name)
    print("Rate of intrest on Fixed deposit:",Bank_Account.ROI_On_FD)

    Bank_Account.DisplayBankinformation()

    User1 = Bank_Account()
    User2 = Bank_Account()

    User1.CreateAccount()
    User2.CreateAccount()

    User1.DisplayAccountInfo()
    User2.DisplayAccountInfo()

    User1.Deposit()
    User2.Deposit()

    print("Ammount of {} after deposit is {}:".format(User1.Name,User1.Amount))
    print("Ammount of {} after deposit is {}:".format(User2.Name,User2.Amount))

    User1.Withdraw()
    User2.Withdraw()

    print("Ammount of {} after withdraw is {}:".format(User1.Name, User1.Amount))
    print("Ammount of {} after withdraw is {}:".format(User2.Name, User2.Amount))
if __name__=="__main__":
    main()