# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
credit_card = '9876-5432-1012-3456'

print(credit_card[0]) #9
print(credit_card[-1]) #6
print(credit_card[3:9]) #6-5432
print(credit_card[:6]) #9876-5
print(credit_card[5:]) #5432-1012-3456
print(credit_card[-9:]) # 1012-3456
print(credit_card[::2]) #step by 2
print(credit_card[::-1]) # Reverses the string
print(credit_card[3:17:3]) #64-13