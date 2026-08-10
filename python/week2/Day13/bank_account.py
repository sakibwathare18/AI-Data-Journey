class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name 
        self.balance = balance 

    def deposit(self, amount):

        if amount > 0 :
            self.balance += amount
            print("Deposit Successful.")
        else :
            print("Invalid Amount.")

    def withdraw(self, amount):

        if amount < 0 :
            print("Invalid Amount.")
        elif amount > self.balance :
            print("Issufficient Balance")
        else :
            self.balance -= amount
            print("Withdrawal Successful.")

    def show_balance(self):
        print("Account Holder :",self.name)
        print("Balance :",self.balance)

    def transfer(self, other_account, amount):

        if amount <= 0 :
            print("Invalid Transfer Amount.")
        elif amount > self.balance:
            print("Issufficient Fund.")
        else :
            self.balance -= amount
            other_account.balance += amount
            print("Fund Transfer Successfull.")

# create account
account1 = BankAccount("Sakib",5000)
account2 = BankAccount("Ali",3000)

# tranfer
account1.transfer(account2,1000)

# # deposit 
# account1.deposit(1000)

# # withdraw
# account.withdraw(500)

# display
account1.show_balance()
account2.show_balance()