# Collections: A "Single" variable used to store multiple values
# List = [] ordered and changeable. Duplicated OK
# Set = {} unordered and immutable. No duplicates. Add/Remove OK
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

#LIST
# A list is a non-homogeneous data structure that 
# stores the elements in columns of a single row or multiple rows.

# The list can be represented by []

# The list allows duplicate elements

# A list can be created using the list() function

# A list is mutable i.e we can make any changes in the list.

# List is ordered
fruits = ["apple", "orange", "banana", "grapes"] 
print(fruits[0::2]) # You can use the index operator with collections much like strings.

for fruit in fruits:  # Iterating over a list
    print(fruit)

print(len(fruits)) 

if "apple" in fruits:
    print("Apple is in my list.")

fruits.append("coconut")  # Add an item. Works like push onto stack
print(fruits)
fruits.remove("apple")  # Remove an item
print(fruits)
fruits.insert(1, "litchi")  # Adds an item at any index
print(fruits)
fruits.sort() # sorts fruits in alphabetical order
print(fruits)
poppedFruit = fruits.pop() # Works like pop out of stack
print(fruits, poppedFruit)
fruits.reverse() # reverses the current order
print(fruits)
index = fruits.index("litchi") # Gives you the index of litchi. Returns a valueError id the element is not present in the list.
print(index)
fruits.append("coconut")  # Add a duplicate item
print(fruits)
print(fruits.count("coconut"))  # Returns to count of the element
fruits.clear() # Clears the list
print(fruits)

print(help(fruits))