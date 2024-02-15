x=int(input("Enter the 4 digit number:")) 
y=x//1000 #Gives first digit
z=(x//100)%10 #Gives second digit
t=(x//10)%10 #Gives third digit
a=x%10 #Gives fourth digit
print("First digit of number is:",y)
print("Second digit of number is:",z)
print("Third digit of number is:",t)
print("Fourth digit of number is:",a)