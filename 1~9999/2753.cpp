/*#include <iostream>
using namespace std;
int IsLeapYear(int a);
int main() {
		int year;
		cin >> year;
		cout << IsLeapYear(year) << endl;
}
int IsLeapYear(int a)
{
	if (a % 4 == 0 && a % 100 != 0)
		return 1;
	else if (a % 100 == 0 && a % 400 == 0)
		return 1;
	else if (a < 0)
		return 2;
	else
		return 0;
}*/