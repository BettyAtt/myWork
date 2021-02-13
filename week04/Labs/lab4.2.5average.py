# This program reads in numbers
# until the user enters 0
# it will then print them back out again
# and their average
# Author: Betty Attwood

#append adds to the end of a list
# the list is blank so after they add a few numbers
# it creates the list which will be averaged when they 
# enter 0 to close it.

numbers = []

number = int(input("enter number (0 to quit):"))

while number != 0:
    numbers.append(number)  
    # read the next number and check if 0
    number = int(input("enter another (0 to quit): "))

for value in numbers:
    print (value)

# I want average to be a float
average = float(sum(numbers))/len(numbers)
print ("The average is {}".format(average))

