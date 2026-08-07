word = input("Enter an word :")
count = 0
vowels = "aeiouAEIOU"

for i in word:
    if i in vowels:
        count += 1

print(f"Vowels in {word} is {count}")
    
