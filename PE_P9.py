######################################################################################################################
# Project Euler
# Problem 9
# File name: PE_P9.py
# Compile: python PE_P9.py
# Programer: Alexis Lopez
# Description: A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52. There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc. 
# NOTE: This program is just for this special case where a + b + c = 1000. You would need
# to modify the program if you want it to work for a general case.
######################################################################################################################

print(r"Welcome to 'Project Euler' This is problem #9")

# Computing square of the sum of natural numbers
def PythagoreanTriplet():

    # Defining Pythagorean variables
    a = 0
    b = 0
    c = 0
    
    # Defining variables to calculate pythagorean variables
    m = 1
    n = 1
    nextM = m
    
    while True:
        for m in range(m, 1000):
            # Using the formula of all the solutions of the pythagorean equation 
            # (Diophantine eqn, where n = 2)
            a = 2 * m * n
            b = m * m - n * n
            c = m * m + n * n
            
            # We found our objective and we return the variables
            if ((a + b + c) == 1000):
                return a, b, c, (a * b * c)
            
            # If the sum is too large continue to next case by incrementing m
            if ((a + b + c) >= 1000):
                break

            n += 1
            m += 1
            #print(a, b, c)

        nextM += 1    # Checking next case to find the solution to the pythagorean eqn
        m = nextM
        n = 1         # Setting n back to one



if __name__ == "__main__":

    a, b, c, product = PythagoreanTriplet()
    
    print("\nThe pythagorean product(a*b*c) where a + b + c = {} + {} + {} = 1000 is: {}".format(a, b, c, product))

    