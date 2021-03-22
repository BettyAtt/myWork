# Labs 6.1.3 second step of using
# functions in a student management
# program
# Author: Betty Attwood
# Lab creator/Content originator: Andrew Beatty

# copy function created in 1st step
def displayMenu():
    print ("what would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View Students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice

#creating functions for the menu options:
def doAdd():
    # we will fill this in later
    print("in adding")
def doView():
    # we fill this in later
    print("in viewing")

# main program
choice = displayMenu()
while(choice != 'q'):
    # we could do this with the lambda functions
    # I am keeping this basic for the moment
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice !='q' :
        print("\n\nplease select either a, v or q")
    choice=displayMenu()
