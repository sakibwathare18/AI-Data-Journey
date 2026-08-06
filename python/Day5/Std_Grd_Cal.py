name = input("Enter Student Name :")
mark = int(input("Enter Students Mark :"))

if mark >= 90 :
    grade = "A"
elif mark >= 75 :
    grade = "B"
elif mark >= 60 :
    grade = "C"
elif mark >= 40 :
    grade = "D"
else :
    print("Fail")

print("Student Name :",name)
print("Student Mark :",mark)
print("Grade :",grade)