# This Program greets user by variable
# Author: Betty Attwood

name = "Betty"
print('Hello ' + name)

# This won't work because you cannot concat int to string
age = 34
#print ('Your age is ' + age)
print ('your age is ' + str(age))
# other solution is to use format
print ('your age is {}'.format(age) )
print ('Hello {}\tyour age is {}'.format(name, age))
