# see if a file exists

import os

filename = "amIhere.text"

if (os.path.exists(filename)):
    print("file exists")
else:
    with open(filename, "x") as f:
        print("creating the file")