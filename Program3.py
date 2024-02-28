#Write a Python program to guess a number between 1 and 9
import random #imports random module
random1 = random.randint(0,9) #generates a random number which will be stored in variable "random1"
usrinput=int(input("Enter the number you are guessing from 0 to 9:")) #Takes input from user
#using loop until the user gets right randomly generated number
while usrinput!=random1: 
    usrinput=int(input("Guess the number from 0 to 9 till you get it right:"))
print("Well Guessed!")  #if usrinput==random1 then well guesses is printed and loop ends

