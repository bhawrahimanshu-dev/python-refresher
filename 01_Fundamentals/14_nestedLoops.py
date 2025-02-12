# Nested loop: loop inside a loop (Outer, Inner)

# Print the tables from 1 to 10

for x in range(1, 11):
    for y in range(1,11):
        print(f'{x*y}', end="    ")
    print('\n')