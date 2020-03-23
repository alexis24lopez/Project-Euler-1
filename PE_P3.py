######################################################################################################################
# Project Euler
# Problem 3
# File name: PE_P3.py
# Compile: python PE_p3.py
# Programer: Alexis Lopez
# Description: The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# This program finds just the largest prime factor of a number
######################################################################################################################

print(r"Welcome to 'Project Euler' This is problem #3")

def Largest_Prime_Factor(number):
    # Defining variables
    test_number = number    # To keep for later use
    lpf = 1    # Test which prime numbers is divisible by
    
    #for test in range(0, number):
    while (1):
    
        if (number % lpf == 0):
            number = int(number / lpf)
        
        if (number == 1):
            break
        
        lpf += 1
    
    print("\nThe Largest prime factor of", test_number, "is:", lpf)

if __name__ == "__main__":
    Largest_Prime_Factor(600851475143)
