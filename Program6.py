'''Write a Python program to count the number of even and odd numbers in a series of numbers
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5'''
numbers=(1,2,3,4,5,6,7,8,9) #storing the values in tuple named numbers
even=0 #to count the number of even numbers
odd=0 #to count the number of odd numbers
for i in numbers:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1
print("Number of even numbers:",even)
print("Number of odd numbers:",odd)