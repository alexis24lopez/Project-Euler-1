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

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def Largest_Palindrome():

    # Definig storing structures
    number = []
    temp = 0
    reverse = 0
    
    for second in range(100,1000):
        for first in range(100,1000):
            result = second * first
            temp = result
            
            while (temp > 0):
                digit = temp % 10
                reverse = (reverse * 10) + digit
                temp //= 10
            
            if (result - reverse == 0):
                number.append(reverse)
                #print(first, "*", second, "=", result)

            reverse = 0
    
    bubble_sort(number)
    print("\nThe Largest 3-digit number multiplied palindrome is:", number[len(number)-1])

    #print("\nThe Largest 3-digit palindrome is:", result)

if __name__ == "__main__":
    Largest_Palindrome()