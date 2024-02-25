'''Write a Python program to find those numbers which are divisible by 7 and multiples of 5, 
between 1500 and 2700 (both included)'''
i=1500
x=2700
while i<=x:
    if (i%7==0) and (i%5==0):
        print(i,end=" ")
    i=i+1