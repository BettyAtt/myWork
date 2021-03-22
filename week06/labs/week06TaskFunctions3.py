# step 4 of functions lab focus on reading in
# the student name, creating a function for reading in
# the module name and grades (step 5)
# Test the function
# function makes a student dict, print it out to test
# add student dict to list (pass list in)
# test this

students= []
#this will be expanded in next step
def readModules():
    return []

# students are a dict; enter student name by input
# student modules entered by fuction readModules
def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()

# students read in added to students list by append
    students.append(currentStudent)

#test

doAdd(students)

doAdd(students)
print(students)