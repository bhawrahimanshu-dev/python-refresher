# List comprehension offers a shorter syntax when you want to create a new list 
# based on the values of an existing list.


# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

# with list comprehension you can do all that with only one line of code:
# SYNTAX -> newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

doubles = [x*2 for x in range(1, 11) if x%2 is 0]
print(doubles)