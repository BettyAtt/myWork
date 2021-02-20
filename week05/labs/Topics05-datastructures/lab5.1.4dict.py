# This program stores a student name
# and a list of her courses
# and grades in a dict & prints her data
#Author: Betty Attwood

# Dictionaries are used to store data values
#  in key:value pairs.
# Here we have a dict -- 'student' which contains a list,
# which has dicts nestled within it
student = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade":99
        }
        
    ]
}
print ("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t:  {}".format(module["courseName"], module["grade"]) )