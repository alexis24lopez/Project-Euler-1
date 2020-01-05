######################################################################################################################
# Project Euler
# Problem 4
# File name: PE_P4.py
# Compile: python PE_P4.py
# Programer: Alexis Lopez
# Description: A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
######################################################################################################################

print(r"Welcome to 'Project Euler' This is problem #4")

# Sorting the numbers from smallest to biggest
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def Largest_Palindrome():

    # Definig storing structures
    palindrome = []     # Arrays of palindrome numbers
    temp = 0            # A temporaly holder to compute reverse of number
    reverse = 0         # Storing mirror image of the number
    
    for second in range(100,1000):
        for first in range(100,1000):
            result = second * first     # Multiplying all possible 3-digits numbers
            temp = result               #  Keeping a copy of result for later use
            
            # Reversing the result eg. 123 -> 321
            while (temp > 0):
                digit = temp % 10
                reverse = (reverse * 10) + digit
                temp //= 10
            
            # If is a palindrome when substract the original and the reverse
            # it will be zero eg. 121 -> 121 => 121 - 121 = 0
            if (result - reverse == 0):
                palindrome.append(reverse)
                #print(first, "*", second, "=", result)     #uncomment if want to see product of palindrome

            reverse = 0
    
    bubble_sort(palindrome)

    print("\nThe Largest 3-digit number multiplied palindrome is:", palindrome[len(palindrome)-1])

    #print("\nThe Largest 3-digit palindrome is:", result)

if __name__ == "__main__":
    Largest_Palindrome()