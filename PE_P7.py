######################################################################################################################
# Project Euler
# Problem 7
# File name: PE_P7.py
# Compile: python PE_P7.py
# Programer: Alexis Lopez
# Description: By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number? You can find any 'th prime number.
######################################################################################################################
import math

print(r"Welcome to 'Project Euler' This is problem #7")

# Computing square of the sum of natural numbers
def prime(thprime):

    # The first prime is 2
    prime = [2]
    
    # To check if this number is prime?
    isPrime = 3
    addPrime = True

    while (len(prime) <= thprime - 1):
        
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
    
    # Adding offset because list starts with zero
    return prime[i + 1]

if __name__ == "__main__":

    primeNumber = int(input("\nPlease enter the primeth number you want to find: "))
    primeth = prime(primeNumber)
    
    print("\nThe {}th prime number is: {}".format(primeNumber, primeth))