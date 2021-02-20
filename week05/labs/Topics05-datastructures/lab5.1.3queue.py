# This program puts 10 random numbers
# in a queue(list),
# then takes the numbers from the queue
# one at a time, prints it,
# then prints the current numbers still in the queue.

import random
queue=[]
numberOfNumbers=10
rangeTo=100

for n in range(0,numberOfNumbers):
    # here we are appending 10 random ints from range 0-100
    #https://www.w3schools.com/python/ref_list_append.asp
    queue.append(random.randint(0,rangeTo))
print("queue is {}".format(queue))

while len(queue) != 0:
    currentNumber = queue.pop(0)
    # this removes the number at specific position from queque
    #https://www.w3schools.com/python/ref_list_pop.asp
    print ("current Number is {} and the queue is {} ".format(
        currentNumber, queue))
print ("the queue is now empty")