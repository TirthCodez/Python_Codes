c=0
a=1
i=int(input("Enter the starting number:"))
x=int(input("Enter the last number:"))
while i<=x:
    a=1
    c=0
    while a<=i:
        if i%a==0:
            c=c+1
        a=a+1
    if c==2:
        print(i)
    i+=1