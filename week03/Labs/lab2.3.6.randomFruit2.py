# This program prints out a random fruit
#but correctly uses a tuple () not a list []
# Author: Betty Attwood

import random

fruits = ('Kiwi', 'Grapefruit', 'Passionfruit', 'Lemon')

# We want a random number beween 0 and lenght-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("A Random Fruit: {}".format(fruit))