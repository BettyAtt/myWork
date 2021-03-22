# make the fuction readModules

def readModules():
    modules = []
    moduleName = input("\tEnter the first module name (blank to quit):").strip()

# while module is not blank it will be a dict object
#  key/value = module name/grade
    while moduleName != "":
        module = {}
        module["name"]= moduleName
        # not doing error handling yet
        module["grade"]=int(input("\tEnter grade:"))
        modules.append(module)
        #now read the next module name
        moduleName = input("\tEnter next module name (blank to quit):").strip()

    return modules

