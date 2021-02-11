# # This program reads in a students percentage marks
# and prints out corresponding grade rounding up 
# if 10th place is 5 or greater
# else rounding down if 10th place is four or less
# Author: Betty Attwood

#ideas for rounding
#You can either set the ranges to 39.5, 49.5, 59.5 etc
# or add a line to round the input
#percentage = float(input("Please enter the percentage mark:"))

#rounds the percentage to a full number
#mark = round(percentage)


#if n >= 0:
    #rounded = round_half_up(n, decimals)
#else:
   # rounded = round_half_do wn(n, decimals)

#OR import decimal module -- but then which rounding to use?
# Ref: https://realpython.com/python-rounding/


percentage = float(input("Enter the percentage: "))
#print (percentage)

if percentage < 0 or percentage >100:
    # later this will be done with throwing error
    print ("Please enter a number betweem 0 and 100")
elif percentage <40: # we know its greater than 0
    print ("Fail")
elif percentage <50: #between 40 and 49
    print ("Pass")
elif percentage <60: # between 50 and 59
    print ("Merit1")
elif percentage <70: # between 60 and 69
    print ("Merit2")
else: # the only option left is between 70 and 100
    print ("Distinction")
    
        