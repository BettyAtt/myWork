# This program prints out a random number
# Author: Betty Attwood

import random

# hashed to run second part which asks user for range
#number = random.randint(1,10)
#print("here is a random number {}".format(number))

#below asks for range to be input and gives a random number
#but needs the string explaining the random number to be added
#x = int(input("Enter first number of range: "))
#y = int(input("Enter last number of range: "))
#print(random.randrange(x, y))     #Ref:https://www.w3schools.com/Python/ref_random_randrange.asp

x = int(input("Enter first number of range: "))
y = int(input("Enter last number of range: "))
number = random.randrange(x, y)
print("Here is a random number from your range: {}".format(number))

#answer =  int(random.randrange(x, y)
#print("{}".format(answer)})

#print ("A random number between {} and {} is {}".format(x, y, answer))
