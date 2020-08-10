######################################################################################################################
# Project Euler
# Problem 25
# File name: PE_P25.py
# Compile: python PE_P25.py
# Programer: Alexis Lopez
# Description: The Fibonacci sequence is defined by the recurrence relation:
# 		Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5, F6 = 8, F7 = 13, F8 = 21, F9 = 34, F10 = 55, F11 = 89, F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
######################################################################################################################

print(r"Welcome to 'Project Euler' This is problem #25")

def fibonacci(n):
	f1 = 1		# F(n) fibonacci number
	f2 = 0
	count = 1	# Index of fibonacci number
	
	while n > len(str(f1)):
		f1, f2 = f1 + f2, f1
		count += 1

	return count

if __name__ == "__main__":

	number = int(input("\nWhat Fibonacci number you want to find that has the first X's digits?:"))
	print("\nThe first Fibonacci number that has ",number, " digits is: ", fibonacci(number))