# While Loop: Execute some code WHILE the condition remains TRUE

# Example 1:
name = input('Enter your name: ')

while not (name.isalpha()):
    print('Invalid name, please try again.')
    name = input('Enter your name: ')

print(f'Hello {name}')


# Example 2:
age = input('Enter your age: ')

while not (age.isdigit()):
    print('Invalid age, please try again.')
    age = input('Enter your age: ')    

print(f'{name}, you are is {age} years old.')
