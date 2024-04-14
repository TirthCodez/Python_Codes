# Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2
string = input("Enter the string:")
count_number=count_letter=0
for i in string:
    if i.isdigit():
        count_number+=1
    elif i.isalpha():
        count_letter+=1
    else:
        continue
print("Letters ",count_letter)
print("Digits ",count_number)