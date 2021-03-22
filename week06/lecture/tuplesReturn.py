# More messing with functions
# tuples as return types

#Author: Betty Attwood

# this is a function that passes back tuple
def passBackTuple():
    return (1, 2, 3)
# in python it also works without the ()
# it will automatically make it a tuple
    
x, y, z = passBackTuple()

print ("x is", x, "y is", y)