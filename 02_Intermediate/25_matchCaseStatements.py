# A Python match-case statement takes an expression and compares its value to successive patterns 
# given as one or more case blocks. Only the first pattern that matches gets executed. I
# It is also possible to extract components (sequence elements or object attributes) 
# from the value into variables.

def weekday(n):
    match n:
        case 0: return "Monday"
        case 1: return "Tuesday"
        case 2: return "Wednesday"
        case 3: return "Thursday"
        case 4: return "Friday"
        case 5: return "Saturday"
        case 6: return "Sunday"
        case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(7))

# Sometimes, there may be a situation where for more than one cases, a similar action has to be taken. 
# For this, you can combine cases with the OR operator represented by "|" symbol.

def access(user):
    match user:
        case "admin" | "manager": return "Full access"
        case "Guest": return "Limited access"
        case _: return "No access"
print(access("manager"))
print(access("Guest"))
print(access("Ravi"))

