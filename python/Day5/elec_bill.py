unit = int(input("Enter Units :"))
bill = None

if unit <= 100 :
    bill = unit * 5
else :
    bill = unit * 8

print("Total Bill :",bill)