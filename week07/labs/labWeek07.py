# Write a program that counts 
# how many times it has been run.
# store the data (persist) in a txt file.

filename = "count.txt"
def readNumber():
    with open(filename) as f:
        number = int(f.read())
        return number
    # test it
num = readNumber()
print (num)