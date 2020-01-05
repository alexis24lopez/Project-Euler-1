######################################################################################################################
# Project Euler
# Problem 5
# File name: PE_P5.py
# Compile: python PE_P5.py
# Programer: Alexis Lopez
# Description: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
######################################################################################################################

print(r"Welcome to 'Project Euler' This is problem #5")

# Computing the n! number using recursion
def factorial(n):
    if (n == 1):
        return 1
    else:
        return (n * factorial(n-1))

def Divisible_by_all_twenty():

    stop = factorial(20)    # Calling the recursion function to compute 20! and storing on stop

    # Loop to test all numbers that are divisble by firts 20 natural numbers
    for test in range (21, stop + 1):
        if (test % 1 == 0 and test % 2 == 0 and test % 3 == 0 and test % 4 == 0 and test % 5 == 0 and test % 6 == 0 and 
            test % 7 == 0 and test % 8 == 0 and test % 9 == 0 and test % 10 == 0 and test % 11 == 0 and test % 12 == 0 and 
            test % 13 == 0 and test % 14 == 0 and test % 15 == 0 and test % 16 == 0 and test % 17 == 0 and test % 18 == 0 and 
            test % 19 == 0 and test % 20 == 0):
            
            return test
        else:
            continue    # If the if-statement fails then proceed to next number

if __name__ == "__main__":

    number = Divisible_by_all_twenty()
    
    print("\nThe smallest number divided by first 20 numbers is:", number)