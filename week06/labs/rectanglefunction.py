# this program calculates the area of a rectangle
#Author: Betty Attwood

#def Area_Rect(width, height):
    #area = width * height
    #print("\n Area of the rectangle is: " + round(str(area), 2))
    #print("\n Area of the rectangle is: %.2f" %area)

#width = float(input("Enter the width of the rectangle: "))
#height = float(input("Enter the height of a rectangle: "))

#Area_Rect(width, height)

def Area_Rect(w, h):
    a = w * h
    return a
   

width = float(input("Enter the width of the rectangle: "))
height = float(input("Enter the height of a rectangle: "))

print("\n Area of the rectangle is: ", round(Area_Rect(width, height), 2))


   
