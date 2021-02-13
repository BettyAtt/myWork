# This program asks the user to guess a number
# and provides feedback of whether
# the number is higher or lower than the guess
# Author: Betty Attwood

numberToGuess = 27

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess > numberToGuess:
        print("Wrong, try guessing lower")
    
    else: # it can't be > or ==  so must be <
        print("Wrong, try a higher number")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)