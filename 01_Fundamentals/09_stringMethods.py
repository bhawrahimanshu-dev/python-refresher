# Strings in python are surrounded by either single quotation marks, 
# or double quotation marks.

# 'hello' is the same as "hello".

print("Hello World!")

#Multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 

#To get the length of a string, use the len() function.
print(len(a)) #123

#find() Searches the string for a specified value and returns the first position of where it was found
first_occurrence = a.find("o")
print(first_occurrence) #1
# returns -1 if the char is not present


#rfind() Searches the string for a specified value and returns the last position of where it was found
last_occurrence = a.rfind("o")
print(last_occurrence) #106
# returns -1 if the char is not present

# The index() method finds the first occurrence of the specified value.
# The index() method raises an exception if the value is not found.
# The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

# Where in the text is the first occurrence of the letter "e" 
# when you only search between position 5 and 10?:
txt = "Hello, welcome to my world."
x = txt.index("e", 5, 10)
print(x)


# capitalize()	Converts the first character to upper case
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

# upper()	Converts a string into upper case
txt = "hello, and welcome to my world."
x = txt.upper()
print (x)

# lower()	Converts a string into lower case
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)

# isdigit()	Returns True if all characters in the string are digits
txt = "5080080"
x = txt.isdigit()
print("isdigit?",x)
#returns false if it is a float

# isalpha()	Returns True if all characters in the string are in the alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)
#returns false if there is sapce character in the string 

# count()	Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print("Count of the word \'apple\' in the string \'I love apples, apple are my favorite fruit\': ",x)

# replace()	Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)