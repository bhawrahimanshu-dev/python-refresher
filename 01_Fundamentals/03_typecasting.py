#Typecasting:  The process of converting the variable from one datatype to another.
#              str(), int(), float(), bool()

name = "Himanshu"
age = 26
cgpa = 8.2
is_student = True

print(type(name))
print(type(age))
print(type(cgpa))
print(type(is_student))

cgpa = int(cgpa)  # Trucates the portion after decimal
print(cgpa)

age = str(age)
print(type(age))
print(age)  

#age += 1 #TypeError: can only concatenate str (not "int") to str

age = float(age)
print(age)

name = bool(name) # Only if our string was emty, it would have given a false
print(name)


