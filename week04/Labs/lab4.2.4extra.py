# This program asks the user to guess a number
# and provides feedback of whether
# the number is higher or lower than the guess
# Author: Betty Attwood


import random
numberToGuess = random.randint(0, 100)

#Ref https://pynative.com/python-random-randrange/#:~:text=For%20example%2C%20random.,number%20from%20the%20inclusive%20range.
guess = int(input("Please guess a number fom 0 to 100:"))
while guess != numberToGuess:
    if guess > numberToGuess:
        print("Wrong, try guessing lower")
    
    else: # it can't be > or ==  so must be <
        print("Wrong, try a higher number")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)