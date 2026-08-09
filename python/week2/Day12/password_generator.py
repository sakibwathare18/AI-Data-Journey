def password_gen():   
    import random
    import string

    charachter = string.ascii_letters + string.digits

    password = ""

    for i in range(8):
        password += random.choice(charachter)

    print("Password :",password)