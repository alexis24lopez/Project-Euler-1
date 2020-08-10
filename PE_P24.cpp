/*********************************************************************************************************************
* Project Euler
* Problem 24
* File name: PE_P24.cpp
* Compile: g++ PE_P24.cpp
* Programer: Alexis Lopez
* A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits
* 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
* The lexicographic permutations of 0, 1 and 2 are: 012   021   102   120   201   210
* What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
*********************************************************************************************************************/
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;
int factorial(int n);

int main(){

	int permutation_digits, count = 0;
	string number = "";
	int stop = 0;
	
	cout << "How many digits does your permutation have?: ";
	cin >> permutation_digits;
	
	while (permutation_digits < 2) {
		cout << "\nPlease enter a number bigger or equal to two: ";
		cin >> permutation_digits;
	}
	
	cout << "\nAt what lexicographic permuation do you want to stop?: ";
	cin >> stop;
	
	while(stop > factorial(permutation_digits)){
		cout << "lexicographic stop is out of range, choose a new one @ or below " << factorial(permutation_digits) << ": ";
		cin >> stop;
	}
	for (int i = 0; i < permutation_digits; i++){
		number += to_string(i);
	}
	
	do{
		//cout << number << endl;
		count++;
		
		if (count == stop){
			cout << "\nThe " << stop << "'th lexicographic permutation is: " << number << endl;
		}
		
	} while (next_permutation(number.begin(), number.end()));
	
	cout << "\nThe number of permutations are: " << count << endl;
	return 0;
}
int factorial(int n)
{
	if (n > 1){
		return n * factorial(n - 1);
	}
	else{
		return 1;
	}
}
