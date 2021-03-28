def Div_Func(a,b):
    while b != 0:
        c = a / b
    if c == 0:
        print("Error. Please enter a divisor other than zero.")
    break
        
    return c

varA = float(input("Enter an integer for the divident: "))
varB = float(input("Enter an integer for the divisor: "))

#print("\n Area of the rectangle is: ", round(Area_Rect(width, height), 2))
print(varA, "divided by ", varB, "equals", Div_Func(varA, varB))
