# Read in a number and add one to it
# Author: Betty Attwood

#number = input  ('please enter a number:')
#newNumber = number + 1
#print ('{} plus one is {}' .format(number, newNumber))
# doesn't work because can't add 1 to string

# we must convert the str so that input returns to an int
number = int(input  ('please enter a number:'))
newNumber = number + 1
print ('{} plus one is {}' .format(number, newNumber))