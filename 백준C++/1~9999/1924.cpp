/*#include<iostream>
using namespace std;
int main() {
	int date[13] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
	char day[7][4] = { "SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT" };
	int x, y;
	int sum_date = 0;
	cin >> x >> y;
	for (int i = 0; i < x; i++)
		sum_date += date[i];
	sum_date = sum_date + y;
	cout << day[sum_date % 7] << endl;
	return 0;
}*/