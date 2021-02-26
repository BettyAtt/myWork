# Messing with functions
# Author: Betty Attwood

def cube(num):
    #print("in cube")
    return num ** 3
# nothing prints because you have defined the funcion 
# not run the function - to run you have to call the function

var = cube(10)
print(var)

for i in range(1,11):
    print (i, "cubed is :", cube(i))