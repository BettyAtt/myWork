# This program is to demonstrate files
# follow along to the lecture
# Author Betty Attwood
# Credit Andrew Beatty's code

with open(".\lecture1.txt", "w") as f:
    print ("create a file")
    # mode r won't work, as won't r+
    # 'a' append mode will work, 
    # x wont work as file exists

with open("textData.txt", "rt") as f :
    #data = f.read(2)
    #print (data)
    for line in f:
        # includes each of the lines for f
        print("we got: ", line.strip()) 
        # strip gets ride of spaces & carriage returns

# writing to a file
#with open("output.txt", "wt") as f:
with open("output.txt", "at") as f:
    f.write("boo hoo\n")
    #chaning the above will overwrite the file
    # if you don't want to over write use append
    print("my data", file=f)