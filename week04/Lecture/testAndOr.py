# Messing with Ands and Ors
# Lecture follow along
# Author: Betty Attwood

number = -1
# brackets just for clarity
if (number >=0) and (number <= 100):
    print("valid")

# below logic is incorrect - can never be true
# if number= -1 nothing prints
# this is bc 1st part true 2nd false
# true + false = false boolean algebra
#if (number <=0) and (number >= 100) :
    #print("stop")
#else:
    #print("go")
    
# instead do OR
if (number <=0) or (number >= 100) :
    print("stop")
else:
    print("go")