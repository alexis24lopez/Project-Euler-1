######################################################################################################################
# Project Euler
# Problem 14
# File name: PE_P14.py
# Compile: python PE_P14.py
# Programer: Alexis Lopez
# Description: The following iterative sequence is defined for the set of positive integers:
#       n → n/2 (n is even)
#       n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
#           13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
# Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
######################################################################################################################

print(r"Welcome to 'Project Euler' This is problem #14")

# Computing square of the sum of natural numbers
def collatz(under):

    lenght = []
    count = 1
    nextNumber = 2
    
    for number in range(2, under):

        while True:
        
            if (number == 1):
                #print("number {} and count {}".format(nextNumber, count))
                lenght.append(count)
                break
            
            if (number % 2 == 0):
                number /= 2
                count += 1

            else:
                number = 3 * number + 1
                count += 1
            
        count = 1
        nextNumber += 1
        number  = nextNumber
        
    return lenght.index(max(lenght)) + 2, max(lenght)



if __name__ == "__main__":

    under = int(input("\nPlease enter the starting number under what number you want to check: "))
    number, collatzLenght = collatz(under)

    print("\nThe number with the largest sequence under one million is : {}, that has {} numbers".format(number, collatzLenght))
    