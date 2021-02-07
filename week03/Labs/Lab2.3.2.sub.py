# This program ask for two numbers to be input 
# and the prints the first subtracted from the second and answer
# Author: Betty Attwood

# input reads in a string so we need to convert into an int
# so we can perform mathematical operations

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = x-y
print("{} minus {} is {} ".format(x, y, answer))
