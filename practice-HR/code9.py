class BankAccount:
    #balance=0
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self,amount):
        self.balance+=amount
        print(self.name, "Your balance is : ",amount)

account = BankAccount("Piyush")
account.deposit(1000)
