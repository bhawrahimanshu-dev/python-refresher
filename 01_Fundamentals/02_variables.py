#Variable : A re-usable container for a value (Integer, String, Boolean, Float).

#String
firstName = "Himanshu"
lastName = "Bhawra"
email = "hi****hu.bhawra999@fake.com"

#Integers
age = 26

#Price
cgpa = 8.2

#Bool
is_student = True

print(f'Hello {firstName} {lastName}. \nYou are {age} years old. \nYour email is {email}. \nYour cgpa in college was {cgpa}.')

if is_student:
    print(f"{firstName} is a student.")
else:
    print(f"{firstName} is not a student.")


