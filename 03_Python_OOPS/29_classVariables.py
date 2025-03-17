# Class Variables =  Shared among all instances of a class
#                    Defined outside the constructor
#                    Allows you to share the data from all objects created from that class

class Student:
    
    graduationYear = 2019
    numStudents = 0

# When we create an object this code will always be executed.
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # We can take the numStudents variable and 
        # increment it by 1 each time we create an object.
        Student.numStudents += 1

student1 = Student("Himanshu", 27)
student2 = Student("Kamalpreet", 28)

print(student1.name)
print(student1.age)
print(Student.graduationYear) #  Always access class variables using class name to enhance readabilityb of the code and avoid any confusions.

print(student2.name)
print(student2.age)
print(Student.graduationYear) #  Always access class variables using class name to enhance readabilityb of the code and avoid any confusions.


# Gives you number of times an object has been created from the class
print(Student.numStudents)