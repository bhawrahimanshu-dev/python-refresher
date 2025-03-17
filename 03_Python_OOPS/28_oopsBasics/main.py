from car import Car

# Creating an object using the constructor method.
car1 = Car("Hyundai", 2007, "Rearth", False)

print(car1)  # Gives you the memory address of where this object is located.

print("Model", car1.model)
print("For Sale? ", car1.for_sale)

car2 = Car("Mahindra", 2025, "Deep Blue", True)

print(car2.model)
print(car2.color)


car1.drive()
car2.drive()

