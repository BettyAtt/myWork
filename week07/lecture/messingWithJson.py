# This is a follow along
# for lecture on JSON
# Author: Betty Attwood
# Copying: Andrew Beatty

#JSON = JavaScript Object Notations,
# a handy way of storing objects
# pickle allows storing of complicated
#  objects such as those that have functions 
# in them which is not very secure if you are
#  passing pickle objects around the place
# json is just storing data

import json
electricBill = {
    'name' : 'andrew',
    'amount' : '999'
}

# could store as a file 2 ways: as just text 
# but reading it in won't work as well 
# or javaScript Object Notation -- import Json
# we will look at dump and load

#with open("storeData.json", "wt") as f:
#    json.dump(electricBill, f)

with open("storeData.json", "rt") as f:
    readDict = json.load(f)
    print(readDict["name"])
    # if we comment out the above, 
    # it still prints andrew because
    # it is still stored in json file