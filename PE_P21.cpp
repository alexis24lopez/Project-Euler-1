/*********************************************************************************************************************
* Project Euler
* Problem 4
* File name: PE_P21.cpp
* Compile: python PE_P21.cpp
* Programer: Alexis Lopez
* Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
* If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
* micable numbers. For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
* therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
* Evaluate the sum of all the amicable numbers under 10000.
*********************************************************************************************************************/
#include <iostream>
#include <vector>

using namespace std;

int sumOfDivisors(int &number);

int main(){
	
	unsigned int max_number;
	
	cout << "Welcome to Project Euler Problem 21!\n\n";
	cout << "Please enter under what number you want to add the amicable numbers: ";
	cin >> max_number;
	
	int amicable, amicable2 = 0;
	vector<int> amicable_numbers = {0};		// Store the amicable numbers.
	vector<int> perfect_square = {0};		// Store the perfect squares.
	
	for (int i = 1; i <= max_number; i++){
		// Loop to find all amicable numbers
		amicable = sumOfDivisors(i);			// Sum of divisors of first potential amicable number.
		amicable2 = sumOfDivisors(amicable);	// Sum of divisors of pair of first potential amicable number
		
		// This is a perfect square.
		if (i == amicable == amicable2){
			perfect_square.push_back(i);
			
		} else if(amicable2 == i && amicable != i){ // This are amicable numbers when amicable2 == i. The rest if to filter perfect squares.
			amicable_numbers.push_back(i);			// Storing amicable numbers.
			amicable_numbers.push_back(amicable);
			i = amicable;							// since the pair of first is bigger set the index to tha number.
													// so we look for the next amicable++ and save time by cutting list search.
		}
	}
	
	int sum_amicable = 0;
	
	// Sum all the amicable numbers and display the result.
	for (int i = 0; i < amicable_numbers.size(); i++){
		sum_amicable += amicable_numbers[i];
		//cout << amicable_numbers[i] << endl;
	}
	
	cout << "\nThe sum of the amicable numbers below " << max_number << " is: " << sum_amicable << endl;
	
	return 0;
}

// To find all the divisors of a specific number by brute force. Returns the sum of the divisors.
int sumOfDivisors(int &number){
	
	int sum = 0;
	
	for (int i = 1; i <= number / 2; i++){
		if (number % i == 0){
			//cout << i << " ";
			sum += i;
		}
	}
	
	return sum;
}
