cart = []
while True :

    item = input("Enter Items (Type 'done' to finish) :")

    if item.lower() == "done":
        break
    cart.append(item)

print("\nShopping Cart :")

for i in cart:
    print("-",i)