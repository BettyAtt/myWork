# More messing with  functions
# Anonymous functions

#Author: Betty Attwood

#def doubler (num):
    #return num * 2

#def tripler (num):
   # return num * 3
   # ^ these arent needed when we define in
   # the lambda the num taking in 
   # and then the out put doubled or tripled

isMax = False
#if isMax:
    #fun = doubler
    #do the same thing with lambda:

if isMax:
    fun = lambda num : num * 2
    # called anonymous funct 
    # because it doesnt have a name
else:
    #fun = tripler
    fun = lambda num : num * 3

var = fun(10)
print(var)

#why use lamba -- if
# array of dict objects and you want to sort
# there is a built in function sorted() 
#  it will take in an array and sort it

#sorted
list = [22, 33, 11, 1, 44]
print (list)
newList = sorted(list)
print(newList)

# what about arrays of fict keys and values?
#key - take in element out of list 
# and take out what we want to sort from

data = [{'first': 'Guido', 'last': 'Van R', 'YOB': 1956},
        {'first': 'Grace', 'last': 'Atty', 'YOB': 1990},
        {'first': 'Ivan', 'last': 'Dosteovsky', 'YOB': 1974}]

def sortFun(item):
    print("last")
    return item['YOB']

#print (data)
newData = sorted(data, key = lambda item : item['last'])
for item in newData:
    print(item)
print(newData)