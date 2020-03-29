######################################################################################################################
# Project Euler
# Problem 16
# File name: PE_P16.py
# Compile: python PE_P16.py
# Programer: Alexis Lopez
# Description: 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?
######################################################################################################################

print(r"Welcome to 'Project Euler' This is problem #16")

# Computing square of the sum of natural numbers
def sum_power_2(size):

	suma = 2
	suma_digits = 0

	for i in range(1, size):
		suma *= 2

	while (suma != 0):
		suma_digits += suma % 10
		suma =  suma // 10
	
	return suma_digits


if __name__ == "__main__":

    power = int(input("\nPlease enter the power of two you wan to add its digits: "))
    sum = sum_power_2(power)

    print("\nThe sum of 2^{} is: {}".format(power, sum))
    