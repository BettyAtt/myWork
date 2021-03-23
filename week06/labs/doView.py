
options for doView

#print ("Student: {}".format(student["name"]))
#for module in student["modules"]:
    #print("\t {} \t:  {}".format(module["courseName"], module["grade"]) )

def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])