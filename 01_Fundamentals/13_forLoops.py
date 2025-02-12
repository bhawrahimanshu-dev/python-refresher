# for loops = execute a block of code a fixed number of times. 
# You can itterate over a range, string, sequence, etc.

for x in range(1, 101, 3): # start, stop, step
    print(x)   

for x in reversed(range(1, 11)):
    print(x)   

creditCard = '1234-578-9012-3456'
for x in creditCard:
    print(x)

for x in range(1, 20):
    if (x == 9):
        print("using the continue keyword to skip the iteration.")
        print("statement before continue keyword")
        continue
        print("statement after continue keyword")        # will skip the iteration, but not come out of the loop
    else: print(x)

for x in range(1, 20):
    if (x == 9):
        print("using the continue keyword to skip the iteration.")
        print("statement before break keyword")
        break
        print("statement after break keyword")        # will come out of the loop
    else: print(x)

# Countdown timer program in python
import time
myTime = int(input('Enter the time in seconds: '))

for second in range(myTime,0, -1):    
    hours = int(second / 3600)
    minutes = int((second % 3600) / 60)
    seconds = (second % 3600) % 60
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)






