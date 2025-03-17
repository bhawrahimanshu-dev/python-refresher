# Inheritance =  Allows a class to inherit attributes and methods of another class
# Helps with code reuseability and extensibility
# class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK!")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Stuart")

print(dog.name)
dog.speak()
print(cat.name)
cat.eat()
print(mouse.name)
mouse.sleep()


