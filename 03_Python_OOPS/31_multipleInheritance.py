# Multiple Inheritance: Inherit from  more than one parent class
                        # C(A, B)
# Multi Level Inheritance: Inherit from Parent which inherits from another parent
                        # C(B) <- B(A) <- A
class Animal():
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print(f"{self.name} is eating.")
        
    def sleep(self):
        print(f"{self.name} is sleeping.")
            
class Prey(Animal):
        
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal):    
        
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

    
rabbit = Rabbit("rabbit")
hawk = Hawk("Hawk")
fish = Fish("Fish")

rabbit.flee()
rabbit.sleep()
hawk.hunt()
hawk.sleep()
fish.flee()
fish.hunt()
fish.sleep()
