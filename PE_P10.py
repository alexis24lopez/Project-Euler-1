######################################################################################################################
# Project Euler
# Problem 10
# File name: PE_P10.py
# Compile: python PE_P10.py
# Programer: Alexis Lopez
# Description: The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
######################################################################################################################
import math

print(r"Welcome to 'Project Euler' This is problem #10")

# Computing square of the sum of natural numbers
def prime(belowNumber):

    # The first prime is 2
    prime = [2]
    
    # To check if this number is prime?
    isPrime = 3
    addPrime = True

    while (isPrime <= belowNumber):
        
        # finding wheter the number in question is prime
        for i in range(0, len(prime)):
            # if this is true we know the number is composite
            if(isPrime % prime[i] == 0):
                addPrime = False
                break
        
        # If addPrime = false we know it is a composite number
        if(addPrime == True):
            prime.append(isPrime)
            #print("Prime number: ", isPrime)
            
        # Checking the next number
        isPrime += 1
        addPrime = True
    
    # Returning the list of primes
    return prime

def sumOfPrimes(sumBelowPrime):

    # Defining our sum varible
    sum = 0
    
    # Summing all the primes in the list
    for i in range(0, len(sumBelowPrime)):
        sum += sumBelowPrime[i]
    
    # Return the sum of all primes below the specified prime
    return sum

if __name__ == "__main__":

    primeNumber = int(input("\nPlease enter the sum below which prime number you want to find: "))
    PrimeBelowNumber = prime(primeNumber)
    sumPrimes = sumOfPrimes(PrimeBelowNumber)
    
    print("\nThe sum below the {}th prime number is: {}".format(primeNumber, sumPrimes))