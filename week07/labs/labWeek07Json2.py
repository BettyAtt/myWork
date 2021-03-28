import json
filename="testdict.json"

def readDict():
    #this will throw error if file doesnt exist
    with open(filename) as f:
        return json.load(f)

#test the function
somedict = readDict()
print(somedict)