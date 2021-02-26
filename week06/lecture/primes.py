# script for generating primes
# author: Betty Attwood

# there are built in functions for primes
import math
primes = []
upto= 1000

def isPrime(candidate):
    #check if it is a prime
    for divisor in range(2, math.floor(math.sqrt(candidate))):
        #was primes but changed to avoid global variable
        # added import math and changed primes to math.sqrt(candidate)
        # had to add math.floor to avoid the float error
        if candidate % divisor == 0:
            return False
    return True

candidates = range(2,upto+1)
#print(type(candidates))
for candidate in candidates:
    # if it is still a prime
    if isPrime(candidate):
        primes.append(candidate)
print (primes)