/*********************************************************************************************************************
* Project Euler
* Problem 4
* File name: PE_P22.py
* Compile: python PE_P22.cpp
* Programer: Alexis Lopez
* Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
* begin by sorting it into alphabetical order. Then working out the alphabetical value for each name,
* multiply this value by its alphabetical position in the list to obtain a name score.
* For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53,
* is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
* What is the total of all the name scores in the file?
*********************************************************************************************************************/
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
//#include <iomanip>	// To use setw()

using namespace std;

#define MAX 5162 //This is the total number of names in the file.

int main(){
	
	cout << "Welcome to Project Euler Problem 22!\n\n";
	
	// initializing variables. Storing into word.
	string f_name;
	int sum = 0;
	char name[50], junk[5];
	vector<string> word;
	word.reserve(MAX);
	
	// Opening the file to read.
	ifstream names;
	names.open("p022_names.txt");
	
	if (!names){
		cout << "Unable to open file";
		exit(1); //terminate with error
	}
	
	// eliminating the "" and we read a new word every ',' and store just the word in the vector.
	while (names.getline(junk, 50, '"') && names.getline(name, 50, '"')){
		stringstream sstr;
		sstr << name;
		sstr >> f_name;
		word.push_back(f_name);
	}
	 names.close();
	 
	 // Sorting the vector in alphabetical order.
	 sort(word.begin(), word.end());
	 
	 
	 // Multiplying its value for each word. A = 1, B = 2, ... , Z = 26.
	 // Getting its alphabetical value for each word.
	 for (int i = 0; i < word.size(); i++){
		 int sum_name = 0;
		 for (int j = 0; j < word[i].size(); j++){
			 sum_name += word[i][j] - 64;
		 }
		 sum += (sum_name * (i + 1));
		 //cout << i << setw(11) << word[i] << setw(5) << sum_name << setw(12) << sum << endl;
	 }
	 
	 cout << "The sum is: " << sum << endl;
	 
	 // Uncomment to display contents of the vector.
	 /*for (int i = 0; i < word.size(); i++){
		 cout << word[i] << endl;
	 }*/

	return 0;
	
}