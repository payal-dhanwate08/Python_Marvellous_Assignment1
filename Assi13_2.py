class BankAccount:
    ROI=10.5
    def __init__(self):
       print("The Name is:")
       A = input()
       self.Name=A
       print("The Amount is:")
       B=float(input())
       self.Amount=B

    def Deposit(self):
        print("Enter the deposited amount:")
        DAmount = float(input())
        Ans = self.Amount+DAmount
        print("Amount diposited successfully",Ans)

    def Withdraw(self):
        print("Enter amount to withdraw:")
        WAmount = float(input())
        Ans = self.Amount-WAmount
        print("Amount withdraw successfully",Ans)
    
    def CalculateInsert(self):
        interest = (self.Amount*BankAccount.ROI)/100
        print("interest on your amount is :",interest)

    def Display(self):
        print("Name of account holder is :",self.Name)
        print("Enter amount :",self.Amount)

def main():
    obj1=BankAccount()
    obj1.Deposit()
    obj1.Withdraw()
    obj1.CalculateInsert()
    obj1.Display()
    
if __name__=="__main__":
    main()
