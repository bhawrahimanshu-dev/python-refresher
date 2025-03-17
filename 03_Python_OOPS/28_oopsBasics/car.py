# A class in Python is a user-defined template for creating objects. 
# It bundles data and functions together, making it easier to manage and use them. 
# When we create a new class, we define a new type of object. 
# We can then create multiple instances of this object type.

# An Object is an instance of a Class. 
# It represents a specific implementation of the class and holds its own data.


# use the "class" keyword to create the class.
class Car:  
    #  To construct a car object we need a func called constructor
    #  We need the below __init__ dunder method (dunder = Double Underscore) to create 
    # a constructor. This method behaves similar to a function.

    # "self" means, this object that we  are creating right now.
    def __init__(self, model, year, color, for_sale):  
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # Methods are the actions that an object can perform
    def drive(self):
        print(f"You drive the {self.color} {self.model}.")

    def stop(self):
        print(f"You stop the {self.color} {self.model}.")