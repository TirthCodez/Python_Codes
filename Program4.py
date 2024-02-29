'''Write a Python program to construct the following pattern, using a nested for loop.
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
'''
x=int(input("Enter the number:"))
'''runs code from 1 to the number user defined like if user gives 3 it will print
*
**
***
'''
for i in range(1,x+1): 
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")
'''This other for loop is used to print the below pattern after what is already printed
Taking one number less than what user give hence not repeating the last pattern
The output of this will be if user have given x=3
**
*
'''
for i in range(x-1,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print(" ")
    
