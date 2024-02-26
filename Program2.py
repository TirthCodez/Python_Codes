'''Write a Python program to convert temperatures to and from Celsius and Fahrenheit'''
#Equation--> F=(9/5)C+32
#ask user if he is going to enter in celsius or fahrenheit
print('''Enter 1 for Celsius or 2 for Fahrenheit''')
x=int(input("Enter your choice:"))
for i in range(1,x+1): #using for loop in case user gives an invalid choice
    if x==1:
        y=int(input("Enter the temperature in celsius:")) #takes input from user in celsius
        f=((9/5)*y)+32 #x is in celsius so using this equation to convert to fahrenheit
        print("The temp in Fahrenheit is:",f)
        break
    elif x==2:
        z=int(input("Enter the temperature in Fahrenheit:")) #takes input from user in Fahrenheit
        c=(z-32)/(9/5) #x is in fahrenheit so using this equation to convert to celsius
        print("The temperature in celsius is:",c)
        break
    else:
        print("Invalid choice") #if user enter number other than 1 or 2
        print('''Enter 1 for Celsius or 2 for Fahrenheit''')
        x=int(input("Enter your choice:"))
