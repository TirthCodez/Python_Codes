#  Write a Python program to get the Fibonacci series between 0 and 50.
# Note : The Fibonacci Sequence is the series of numbers :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Every next number is found by adding up the two numbers before it.
# Expected Output : 0 1 2 3 5 8 13 21 34
a=0
b=1
sum=a+b
print("The fibonacci series is:",a,b,end=" ") #prints the value 0 and 1 because we dont need to do it in loop
for i in range(1,10): #when adding 9 terms we will get fibonnaci series upto 50
#runs loop from 1 to 9(included) and changes value of a,b and sum everytime loop runs
    sum=a+b #adds the value of a and b and adds it to sum
    a=b #swaps the value of a and changes it to b i.e. updates value of a and changes it to b
    b=sum #updates values of b and changes it to sum
    print(sum,end=" ")