"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isItPrime(n):
    #assummes that n is not 1 or 0

    for x in range(2, int(n/2)):
        if (n % x) == 0:
            return False #since it is divisible by something

    return True

def primes(number_of_primes):

    if number_of_primes == 0 or number_of_primes < 0:
        raise ValueError("Incorrect value entered")

    list = []

    count = number_of_primes
    y = 2
    while count != 0:
        
        if isItPrime(y) == True and (y != 4): 
            count = count - 1
            list.append(y)
            print("Number added to list: " + str(y))
            y = y + 1
        else:
            y = y + 1
    
    return list
