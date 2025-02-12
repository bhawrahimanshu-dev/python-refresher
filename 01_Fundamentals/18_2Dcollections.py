fruits = ['apples', 'bananas', 'oranges', 'litchi', 'grapes']
vegetables = ['radish', 'pumpkin', 'potatoes', 'cabbage']
meat = ['chicken', 'turkey', 'mutton']

groceries = [fruits, vegetables, meat]

print(groceries)

print(groceries[0])

for collection in groceries:
    for item in collection:
        print(item, end = " ")
    print()

# you can create a 2D list, a 2D tuple, a list of tuples, a tuple of lists, a list of sets, a tuple of sets
# sets are not 2D

# 2 Dimensional Keypad

# In this example, we can't use set because it is unordered. tuple or list can be used. 
# Choose tuple wherever possible to reduce the chances of error by accidentally 
# adding/removing an element. Since we don't see and new digits added in the keypad, 
# we can use a tuple.

numPad = ((1,2,3),
          (4,5,6),
          (7,8,9),
          ('*',0,'#'))

for collection in numPad:
    for num in collection:
        print(num, end = " ")
    print()