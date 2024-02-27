'''Write a Python program to convert temperatures to and from Celsius and Fahrenheit(Method-2)'''
#Equation--> F=(9/5)C+32
#Ask user to input temperature as (Integer)F/C e.g. 104F or 23C
temp=input("Enter the temperature:")
number=temp[:-1] #takes integer part from user given number
degree=temp[-1] #takes alphabet part from user
number=int(number)
if degree=="C" or degree=="c": #considers temp is in celsius
    y=((9/5)*number)+32 
    print("The temperature in Fahrenheit is",y)
elif degree=="F" or degree=="f": #considers temp in Fahrenheit
    y=(number-32)/(9/5)
    print("The temperature in celsisu is:",y)
else:
    print("Enter the last alphabet as either F or C")