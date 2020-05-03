#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
#include <vector>

using namespace std;
 
int zeller(int year, int month, int day);
 
 int main()
 {
	int numberOfDay;
	int startYear, endYear = 0;
	int countDay = 0;	// Keep track of how many time the day of week starts on the month.
	
	cout << "Welcome!! \nEnter: 0 = sunday, 1 = monday, ... , 6 = saturday" << endl; 
	cout << "What day of the week you want to count that fell on the first of the month?\nPlease enter which year to what year separated by a space\n";
	cout << "Example I want to compute sunday from 1901 to 2000 the format is: 0 1901 2000\n\nNow enter yours: ";
	cin >> numberOfDay >> startYear >> endYear;
	
	// Check if the number is between the range.
	if (numberOfDay - 6 > 0 || numberOfDay - 6 <= -7){
		cout << "Please enter a number in the range 0 to 6\n";
		return 0;
	}
	
	// Swap numbers if end is smaller than start year.
	if (startYear > endYear){
		startYear = startYear + endYear;
		endYear = startYear - endYear;
		startYear = startYear - endYear;
	}
	
	int copyStartYear = startYear;
	
	// Find all the months where it starts with the specified year.
	for (startYear; startYear <= endYear; startYear++){
		for (int month = 1; month <= 12; month++){
			if (zeller(startYear, month, 1) == numberOfDay){ // Check wheter the month starts with the input day of week.
				countDay++;
			}
		}
	}
	
	vector<string> days{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
	
	cout << "\nThe number of times " << days[numberOfDay] << " started as the first of the month between the years " << copyStartYear << " and " << endYear << " are: " << countDay << endl;
	
	return 0;
 }

int zeller(int year, int month, int day)
 { 
	 if (month <= 2){
		 month += 10;
		 year -= 1;
		 
	}else{
		month -= 2;
	}
	 
	 int century = year / 100;
	 int centuryYear = year % 100;
	 
	 int dayOfWeek = (day + (((13 * month) - 1) / 5) + centuryYear + (centuryYear / 4) + (century / 4) - 2 * century) % 7;
	 
	 //cout << day << setw(4) << month << setw(4) << century << setw(4) << centuryYear << endl;
	if (dayOfWeek < 0){
		dayOfWeek += 7;
	}
	
	 return dayOfWeek;
 }
