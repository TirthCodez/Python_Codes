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
for i in range(1,2):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print(" ")
    for i in range(x-1,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print(" ")
