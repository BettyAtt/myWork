# This program rounds a number
# Rounds will round to the nearest even number
# which can be problematic if accuracy is essential
# Author: Betty Attwood

numberToRound = float(input("Enter a float number:"))
roundedNumber = round(numberToRound)
print ( '{} rounded is {}'.format(numberToRound, roundedNumber))
