# super() = Function used in child class to call the methods from a parent class (Superclass).
#           Allows you to extend the functionality of the inherited methods.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
        
    def describe(self):
        print(f"It's color is {self.color} and it is {'filled' if(self.filled) else 'not filled.'}")
        

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
    # If a child shares a same method with the parent, child's version of the method gets executed 
    # This is called Fucntion Overriding. 
    def describe(self):
        print(f"It is a circle with an area of {3.14*self.radius*self.radius} cm^2")
        # Using super() to extend the functionality of the child's describe method 
        # And execute the parent's describe method inside this method
        super().describe()

class Square(Shape):
    def __init__(self, color, filled, side):
        super().__init__(color, filled)
        self.side = side
        
    def describe(self):
        print(f"It is a square with an area of {self.side * self.side} cm^2")
        # Using super() to extend the functionality of the child's describe method 
        # And execute the parent's describe method inside this method
        super().describe()

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height
        
    def describe(self):
        print(f"It is a triangle with an area of {(self.width * self.height) / 2} cm^2")
        # Using super() to extend the functionality of the child's describe method 
        # And execute the parent's describe method inside this method
        super().describe()
        
circle = Circle(color="Red", filled=False, radius=5)

print(circle.color)
print(circle.filled)
print(circle.radius)
circle.describe()

square = Square(color="Blue", filled=True, side=10)

print(square.color)
print(square.filled)
print(square.side)
square.describe()


triangle = Triangle(color="Green", filled=True, width=7, height=10)

print(triangle.color)
print(triangle.filled)
print(triangle.width)
print(triangle.height)
triangle.describe()

