#Print the table in following format for any number
#E.g. Table of 5
#5 x 1 = 5
#5 x 2 = 10 etc.
number=int(input("Enter the number you want table for:"))
for i in range(1,11):
    print(number," x ",i," = ",number*i)