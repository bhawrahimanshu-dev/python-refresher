#TUPLE
# A tuple is a non-homogeneous data structure that 
# stores the elements in columns of a single row or multiple rows.

# The tuple can be represented by ()

# The tuple allows duplicate elements

# A tuple can be created using the tuple() function

# A tuple is immutable i.e we can not make any changes in the tuple.

# tuple is ordered
fruits = ("apple", "orange", "banana", "grapes")
print(fruits[0::2]) # You can use the index operator with collections much like strings.

for fruit in fruits:  # Iterating over a tuple
    print(fruit)

print(len(fruits)) 

if "apple" in fruits:
    print("Apple is in my tuple.")

index = fruits.index("banana") # Gives you the index of litchi. Returns a valueError id the element is not present in the tuple.
print("index of banana", index)
print(fruits.count("coconut"))  # Returns to count of the element