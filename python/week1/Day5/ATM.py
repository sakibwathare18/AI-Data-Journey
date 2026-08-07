balance = 100000

amount = int(input("Enter Amount to Withdrawal :"))

if amount <= balance :
    print("Withdrawal Successfull.....!")
    balance = balance - amount
    print("Remaining Balance :",balance)
else :
    print("Issufficient Balanece.....!")
    print("Available Balance :",balance)