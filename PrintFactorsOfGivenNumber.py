x=int(input("Enter the number whose factors you want:"))
c=0 #used for printing the number of factors
for i in range(1,x+1,1):
    if x%i==0:
        print(i,end=" ")
        c=c+1
        '''INCREASES THE COUNT FROM 0 WHEN CONDITION IS TRUE IN THE LOOP'''       
    i+=1
print(" ")
print("The number of factors obtained are:",c) #GIVES THE FINAL NUMBER OF FACTORS OBTAINED