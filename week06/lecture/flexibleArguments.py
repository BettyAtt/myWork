# More messing with functions
# flexible arguments
# Author: Betty Attwood

print("hi", 55, [], (), sep=":")
#flexible number of arguments
def average(*numbers):
    sumOf = sum(numbers)
    return sumOf/len(numbers)

ave = average (12, 12, 12, 35647, 666)
print("average is ", ave) 


# flexible number or named arguments
def fun(arg1 = 0, arg2 = 1 ):
     return arg1 - arg2

print (fun(10, 2)) 
# if we print without passing in 
# arguments e.g. fun()it will take the defaults set above

def funkyArgs(**args): 
#takes in any number of named args
    print (args)
funkyArgs()
# returns empty dict object {}

funkyArgs(name="joe", age = 33, courses = [])
# this passes in a variable number of arguments 
# and converts them into a dict object
