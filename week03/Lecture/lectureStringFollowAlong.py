# A Program to demonstrate strings in python
# in my lecture
# Author: Betty Attwood

# How to use a single quote inside a variable
# because three single quotes flags syntax error as it think
# the apostrophe is closing the variable
# change the surrounding single quotes to double
# use the single quote for possession
#name = "Betty's code"
#print (name)

#Option 2: use the escape character (backslash)
# which indicates that character that follows this I mean it to be there
name = 'Betty\'s code'
print (name)

name = "Betty's code " + str(2) # must add str to concat str w/ int
print (name)