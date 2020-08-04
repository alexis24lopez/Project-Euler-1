/*********************************************************************************************************************
* Project Euler
* Problem 23
* File name: PE_P23.cpp
* Compile: g++ PE_P23.cpp
* Programer: Alexis Lopez
* A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
* For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
* which means that 28 is a perfect number. A number n is called deficient if the sum of its proper divisors
* is less than n and it is called abundant if this sum exceeds n. As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
* the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis,
* it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
* However, this upper limit cannot be reduced any further by analysis even though it is known that the
* greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
* Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers
*********************************************************************************************************************/
#include <iostream>
#include <vector>

using namespace std;
#define SIZE 28123
int sumOfDivisors(int &number);

int main(){

	// Storing all the abundant numbers from 12 to 28123
	vector<int> abundant_number;
	vector<int> pos_integer;
	
	int abundant = 0;
	int sum_of_not_abundant = 0;
	int delete_number = 0;
	
	// Looking for all abundant numbers below 28123
	for (int i = 12; i < SIZE; i++){
		abundant = sumOfDivisors(i);
		
		// If is an abundant number store the number
		if (abundant > i){
			abundant_number.push_back(i);
			//cout << i << endl		
		}
	}

	// Initializing array with secuential numbers from 0 to 28123
	for (int k = 0; k < SIZE; k++){
		pos_integer.push_back(k);
	}

	// Find all the possible sum that two abundant numbers could form and delete them for the vector
	for (int i = 0; i < abundant_number.size(); i++){
		for (int j = 0; j < abundant_number.size(); j++){
			delete_number = abundant_number[i] + abundant_number[j];
			
			if (delete_number > 28123){
				continue;
			}
			pos_integer[delete_number] = 0;
		}
	}

	// On the pos_integer should be only the numbers that are not the product of two abundant numbers.
	for (int i = 0; i <= SIZE; i++){
		sum_of_not_abundant += pos_integer[i];
	}
	
	cout << "The sum of all the positive integers which cannot be written as the sum of two abundant numbers is: ";
	cout << sum_of_not_abundant << endl;

return 0;
}

// To find all the divisors of a specific number by brute force. Returns the sum of the divisors.
int sumOfDivisors(int &number){
	
	int sum = 0;
	
	for (int i = 1; i <= number / 2; i++){
		if (number % i == 0){
			sum += i;
		}
	}
	
	return sum;
}
