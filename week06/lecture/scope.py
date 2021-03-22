# more messing with functions
# variable scope
# author: Betty Attwood

var = 10

def cube(num):
    var = 66
    print ("in the fuction var is ", var)
    return num ** 3

cube(22)
print ("outside the function var is ", var)
# if you print (num) it does not work
# as it will say num is not defined b/c
# the scope of num is inside the above function.
# it does carry out beyond it.