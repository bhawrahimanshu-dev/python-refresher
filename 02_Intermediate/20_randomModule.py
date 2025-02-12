import random

low = 1
high = 100
options = ['rock', 'paper', 'scissors']
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'K', 'Q', 'J', 'A']
number = random.randint(low, high)  # Return random integer in range [a, b], including both end points
print(number)

float_number = random.random()  # The random() method returns a random floating number between 0 and 1.
print(float_number)

choice = random.choice(options)  # Returns a list with a random selection from the given sequence
print(choice)

random.shuffle(cards)  # Takes a sequence and returns the sequence in a random order. 
print(cards)  # Shuffle list in place (actual sequence), and return None

