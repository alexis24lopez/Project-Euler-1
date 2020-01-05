######################################################################################################################
# Project Euler
# Problem 6
# File name: PE_P6.py
# Compile: python PE_P6.py
# Programer: Alexis Lopez
# Description: The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.
######################################################################################################################

print(r"Welcome to 'Project Euler' This is problem #6")

# Computing sum of square of natural numbers
def sum_of_squares(n):

    sum = 0
    
    # Summing and squaring the numbers eg. 1^2 + 2^2 + ... + n^2
    for i in range(1, n+1):
        sum += i*i
    
    return sum

# Computing square of the sum of natural numbers
def square_of_the_sum(n):

    sum = 0
    
    # Summing all natural numbers
    for i in range(1, n+1):
        sum += i
    
    # Squaring the sum of natural numbers eg. sum^2
    sum *= sum
    
    return sum

if __name__ == "__main__":

    sumSquares = sum_of_squares(100)
    squareSum  = square_of_the_sum(100)
    
    print("\nThe difference between the sum of squares and square of sum is:", squareSum - sumSquares)