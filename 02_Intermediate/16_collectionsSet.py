#SET
# The set data structure is non-homogeneous but stores the elements in a single row.

# The set can be represented by {}

# The set does not allow duplicate elements

# A set can be created using the set() function

# A set is mutable i.e we can make any changes in the set.

# List is unordered
fruits = {"apple", "orange", "banana", "grapes"} 

for fruit in fruits:  # Iterating over a set
    print(fruit)

print(len(fruits)) 

if "apple" in fruits:
    print("Apple is in my list.")

fruits.add("coconut")  # Add an item. Does not work like push onto stack as it is unordered
print(fruits)
fruits.remove("apple")  # Remove an item
print(fruits)
poppedFruit = fruits.pop() # pops out the first element in the set, since set is unordered, it can be random
print(fruits, poppedFruit)
fruits.add("coconut")  # Can't add a duplicate item
print(fruits)
fruits.clear() # Clears the set
print(fruits)