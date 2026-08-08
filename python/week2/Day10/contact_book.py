contacts = []

def add():
    name = input("Enter Name:")
    phone = input("Enter Phone No. :")
    email = input("Enter E-Mail :")

    contact_book = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact_book)

    print("Added Successfully...")

def view():
    if not contacts:
        print("Add Contact First...")
        return

    for contact in contacts:
        print(f"Name : {contact['name']} | Phone : {contact['phone']} | E-Mail : {contact['email']}")

def search():
    if not contacts:
        print("Add Contact First...")
        return

    name = input("Enter Name:")
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Found..")
            print(f"Name : {contact['name']} | Phone : {contact['phone']} | E-Mail : {contact['email']}")
            found = True
    if not found:
        print("Not Found")

def delete():
    if not contacts:
        print("Add Contact First...")
        return
    name = input("Enter Name to Delete :").lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("Contact Deleted..")
        else :
            print("Contact not found")

while True:
    print("\n1.Add Contact\n2.View Contacts\n3.Search Contacts\n4.Delete Contact\n5.Exit")
    choice = input("Enter Choice :")

    if choice == "1" :
        add()
    elif choice == "2" :
        view()
    elif choice == "3" :
        search()
    elif choice == "4" :
        delete()
    elif choice == "5" :
        print("Byee...")
        break
    else :
        print("Invalid Choice")
