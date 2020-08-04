/*********************************************************************************************************************
* Project Euler
* Problem 4
* File name: PE_P20.cpp
* Compile: python PE_P20.cpp
* Programer: Alexis Lopez
* Special Thanks for the geeks for geeks on helping on the code for multiplication.
* Description: n! means n × (n − 1) × ... × 3 × 2 × 1. For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
* and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
* Find the sum of the digits in the number 100!
*********************************************************************************************************************/
#include <iostream>

using namespace std;

int multiply(int &x, int res[], int &res_size);

#define TOP 2600
 
int main(){
	
	int number;
	
	cout << "Welcome to Project Euler Problem 20!\n";
	cout << "Please enter the factorial number you want its digits to add: ";
	cin >> number;
	
	if (number > 1){

		int fact[TOP];
		unsigned int fact_sum = 0;
		int factSize = 1;
		
		fact[0] = 1;
		
		for (int i = 2; i <= number; i++){
			factSize = multiply(i, fact, factSize);
		}
		
		for (int i = factSize - 1; i >= 0; i--){
			fact_sum += fact[i];
			//cout << fact[i];	//To display the factorial
		}
		
		cout << "\nThe sum of the digits of " << number << "! is: " << fact_sum << endl;
	
	} else {
		cout << "\nThe factorial of 1 is: 1\n";
	}
	
	return 0;
}

int multiply(int &x, int res[], int &res_size) 
{ 
    int carry = 0;  // Initialize carry 
  
    // One by one multiply n with individual digits of res[] 
    for (int i = 0; i < res_size; i++) 
    { 
        int prod = res[i] * x + carry; 
  
        // Store last digit of 'prod' in res[]   
        res[i] = prod % 10;   
  
        // Put rest in carry 
        carry  = prod / 10;     
    } 
  
    // Put carry in res and increase result size 
    while (carry) 
    { 
        res[res_size] = carry % 10; 
        carry = carry / 10; 
        res_size++; 
    }
	
    return res_size; 
} 

