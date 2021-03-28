import json
# students= [] is the array we store everything in
students= []
filename="students.json"
def writeDict(obj):
    with open(filename, 'wt') as f:
        json.dump(obj,f)

def readDict():
    # this will throw an error if the file does not exist
    # it should readly just return an empty array
    # we can do this later
    with open(filename) as f:
        return json.load(f)

def displayMenu():

    print ("what would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View students")
    print ("\t(s) Save students")
    print ("\t (l) Load students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/s/l/q):").strip()
    return choice

# students are a dict; enter student name by input
# student modules entered by fuction readModules
def doAdd():
    currentStudent = {}
    currentStudent["name"]=input("Enter name :")
    currentStudent["modules"]= readModules()
# students read in added to students list by append
    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first module name (blank to quit):").strip()

# while module is not blank it will be a dict object
#  key/value = module name/grade
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # not doing error handling yet
        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        #now read the next module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules

def displayModules(modules):
    print ("\tModule Name \tGrade")
    for module in modules:
        print("\t{}  \t\t{}".format(module["name"], module["grade"]))

def doView():
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

def doSave():
    writeDict(students)
    print("students saved")

def doLoad():
    #we are chaning the global variable students
    # so we need to indicate this
    global students
    students = readDict()
    print ("students loaded")


# main program
choice = displayMenu()
while(choice != 'q'):
    # we could do this with the lambda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice == 'l':
        doLoad()
    elif choice == 's':
        doSave()    
    elif choice !='q' :
        print("\n\nplease select either a, v, s, l or q")
    choice=displayMenu()