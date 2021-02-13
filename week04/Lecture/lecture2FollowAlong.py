# This is just follow along for while loops
# Author: Betty Attwood

# while condition
#   statements

#count = 0
#while count < 10:
    #print(count)
    #count += 1

#blast off program
#counter control
count = 10
while count >= 0:
    print(count)
    count -= 1
print("Blast Off")

#sentinel controlled loop
val = input("enter something (q to quit):")
while val != 'q':
    print ("you said: " + val) #do something
    val = input ("(q to quit):")
print ("goodbye")

