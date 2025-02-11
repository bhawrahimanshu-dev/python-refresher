# format specifiers = {:flags} format a value based on what
#                              flags are inserted

# . (number)f = round to that many decimal places (fixed point)
# : (number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

# These are not really used in real life scenarios but good to know. Mostly,
# the basic form of format specifiers would be enough.

money = 5000
print(f"I have ₹{money:,.2f} rupees.")