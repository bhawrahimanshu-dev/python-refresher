def happy_birthday(name, age):
    print(f"Happy birthday {name}!")
    print(f"You are {age} years old.")

happy_birthday('Himanshu', '26')  # Known as arguments
happy_birthday('Shreya', '25')

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# There are 4 types of arguments
# 1. Positional 2. DEFAULT 3. Keyword 4. Arbitrary

# 1. Positional Arguments
def add(num1, num2):
    return(f'The sum of {str(num1)} and {str(num2)} is {str(num1+num2)}')

print(add(5,10)) 

# 2. Default Arguments

# default arguments = A default value for a certain parameters  
#                     default is used when the argument is omitted
#                     makes your functions more flexible by reducing the number of args

def net_price(list_price, discount = 0, tax = 0.18):
    return list_price * (1-discount) * (1+tax)

print(net_price(500))
print(net_price(500, 0.10))
print(net_price(500, 0.05, 0.27))

import time

def count(end, start = 0):  # Non-default argument follows default argument
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print('Done')

# count(10)
# count(30, 15)

# 3. Keyword arguments  

# keyword arguments = An argument preceded by an identifier  
#                     helps with readability, order of arguments does not matter

def greetings(salutation, title, fname, lname):
    return f'{salutation}! {title} {fname} {lname}'

# Positional argument cannot appear after keyword arguments
print(greetings('Hello', title='Mr.', lname='John', fname='James'))

# A lot of built-in functions have keyword args
for x in range(1, 11): 
    print(x, end=" ")

print(1,2,3,4,5, sep='-')


# 3. Arbitrary arguments  

# Arbitrary arguments = "varying amount of arguments" 
# *args     = allows you to pass multiple non key arguments
# **kwargs  = allows you to pass multiple keyword arguments
# *         = unpacking operator

def add(*args):
    print(type(args)) # Takes all the arguments passed and packs them into a tuple
    total = 0
    for arg in args:  # Loop through the args tuple
        total += arg
    return total

print(add(1,2,3,4,5,6,7,8,9,0))

def display_name(*args):
    for arg in args:  # Loop through the args tuple
        print(arg, end=" ")

print("Dr.", "Spongebob", "Squarepants", "III")


def print_address( ** kwargs):
    print(type(kwargs))  # kwargs is a dict()
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St.",
                apt="100",
                city="Detroit",
                state="MI",
                zip="54321")


def shipping_label(*args, ** kwargs):  # args neeed to go before kwargs, always!
    for arg in args:  # Loop through the args tuple
        print(arg, end=" ")
    print()
    for key, value in kwargs.items():
        print(f"{key}: {value}")


shipping_label("Dr.", "Spongebob", "Squarepants", "III",
                street="123 Fake St.",
                apt="100",
                city="Detroit",
                state="MI",
                zip="54321")