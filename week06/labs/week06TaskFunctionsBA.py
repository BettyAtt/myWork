# the array we store everything in
# pulling the pieces together

# From Andrew Beatty's lab

def displayMenu():
    print ("what would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

# students are a dict; enter student name by input
# student modules entered by fuction readModules
def doAdd(students):
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

# main program
students = []
choice = displayMenu()
while(choice != 'q'):
    # we could do this with the lambda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView()
    elif choice !='q' :
        print("\n\nplease select either a, v or q")
    choice=displayMenu()