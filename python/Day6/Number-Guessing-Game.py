secret = 7

guess = 0

while guess != secret:

    guess = int(input("Guess number: "))

    if guess == secret:
        print("Correct!")

    else:
        print("Try again")