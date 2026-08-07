word = input("Enter Word :")
reversed_text = ""

for char in word:
    reversed_text = char + reversed_text

if reversed_text == word :
    print("Palindrome")
else :
    print("Not Palindrome")