######################################################################################################################
# project Euler
# Problem 1
# File name: PE_P1.py
# Compile: python PE_p1.py
# Programer: Alexis Lopez
# Description: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
######################################################################################################################

print(r"Welcome to 'Project Euler' This is problem #1")

# Defining variables
stop = 1000    # Find sum up to the value of number
sum = 0      # Store the sum of multiples of 3 or 5
start = 1    # Start at 1 and end at stop value

# Finding the values of multiples of 3 or 5 and storing the sum of those values.
while (start < stop):

    if(start % 3 == 0 or start % 5 == 0):
        sum += start
    
    start += 1
    
print("\nThe result is: ", sum)