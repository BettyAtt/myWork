# This tuple stores the months of the year
# and another stores the summer months.
# The program prints out the summer months one at a time.

months = ( 
    "January","February",
    "March", "April", "May", "June", 
    "July", "August", "September", 
    "October", "November", "December"
)
summer = months [4:7]
 # through seven because it will pull -1 e.g. 4-6

for month in summer:
     print(month)
