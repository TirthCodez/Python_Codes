#  Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".
# Sample Output :
# 1
# 2
# fizz
# 4
# buzz
for i in range(1,51): #iterates numbers from 1 to 50
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0: #checks if number is divisible by 3 only
        print("fizz")
    elif i%5==0: #checks if number is divisible by 5 only
        print("buzz")
    else:
        print(i)