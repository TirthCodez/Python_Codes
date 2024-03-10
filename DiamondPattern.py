n=5
for i in range(1,n+1):
    for k in range(0,n-i+1):
        print(" ",end=" ")
    for j in range(1,i):
        print(" * ",end=" ")
    print(" ")
for i in range(1,n+1):
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(6,i,-1):
        print(" * ",end=" ")
    print(" ")