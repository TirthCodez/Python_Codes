a=0
b=1
x=int(input("Enter the number:"))
print(a,b,end=" ")
for i in range(3,x+1):
    sum=a+b
    a=b
    b=sum
    print(sum,end=" ")