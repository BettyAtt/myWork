# This program converts a float amount of dollars
# and returns that absolute amount in cent.
# It first converts float to absolute
# Then converts absolute dollars to cents
# Author: Betty Attwood



number = float(input("Enter dollar amount:"))
absoluteValue = abs(number)
cents = int(absoluteValue * 100) #used float first but ended up with $ -8.64  = ¢ 864.0 
print("$",number, " = ¢", cents)
# Reference:www.csharp-console-examples.com/programming-languages/python3/convert-dollars-to-cents-in-python/