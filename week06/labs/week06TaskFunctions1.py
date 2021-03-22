# This is weekly task Week 06
# Quiz & Student Management Program
# Author: Betty Attwood

# Quiz 1. a. the program wouldn't print anything
# as it just defined the function of yo(a)
# 1. b. print(yo(3)) or var= yo(3)
#                       print(var)

# Student Management Program

def displayMenu():
    print ("what would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View Students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice
# test the function
choice = displayMenu()
print("you chose {}".format(choice))