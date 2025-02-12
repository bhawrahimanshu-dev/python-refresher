# dictionary

# A dictionary is a non-homogeneous data structure that stores key - value pairs.

# The dictionary can be represented by {}

# The dictionary does not allow duplicate keys

# A dictionary can be created using the dict() function

# A dictionary is mutable i.e we can not make any changes in the dictionary.

# dictionary is ordered

capitals = {"India":"New Delhi"
            ,"USA":"New York"
            ,"China":"Beijing"
            ,"Russia":"Moscow"
            ,"Bangladesh":"Dhaka"}

print(dir(capitals))

print(capitals.get("USA")) # Returns None if key is not present in the dictionary
capitals.update({"Germay":"Berlin"}) # Add a new key value pair
print(capitals)

capitals.update({"USA":"Washinton D.C."}) # Update an existing key value pair
print(capitals)

capitals.pop("China") # pops out the key:value pair where key = "China"
print(capitals)

capitals.popitem() # pops out the latest key value pair
print(capitals)

keys = capitals.keys() # Lists all the keys present in the dict. Keys is an object here. They are iterable.
print(keys)

values = capitals.values() # Lists all the values present in the dict. Values is an object here. They are iterable.
print(values)

items = capitals.items() # items object is a list of tuples
print(items)
for key, value in capitals.items():
    print(f"{key}:{value}")

capitals.clear() # clears the dict