# This program reads in a string and strips
# any leading or trailing spaces.
# It also coverts all the letters to lower case
# and outputs the length of the original string
# and the normalised one.

# Author: Betty Attwood

# .strip() removes white space before and after string
# .lower() changes all characters to lower case
rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()

# len() to get length of raw then normalised strings
lengthOfRawString = len(rawString)
lengthOfNormalisedString = len(normalisedString)

print("That string normalised is :{}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(lengthOfRawString, lengthOfNormalisedString))

