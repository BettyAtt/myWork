# Follow along with lecture
#Messing around with variable types
# Author: Betty Attwood

#age = 'hello'
#print (type(age))

#ageOfPatient = {}
#age = '3'
#print(type(ageOfPatient))
#print(type(age))
#give error because its adding int to string
#print("you are " + age )

# convert int to str
#print("you are " + str(age) )

#convert a string into an integer
# by placing ' ' around age = '3'

ageOfPatient = {}
age = '3'
# need to convert type to str so we can concate it to the message
# formatting is another option instead of type casting
print ("type of ageOfPatient is :" + str(type(ageOfPatient)))
print ("type of age is:" + str(type(age)))
print ("you are " + str(age))
#need to convert age from str to int so I can add 1
nextYear = int(age) + 1
print ("Next year you will be " + str(nextYear))