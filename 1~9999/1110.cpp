/*#include<iostream>
using namespace std;
int main() {
	int n, sum=0, count = 0, result = 0;
	cin >> n;
	sum = n;
	do {
		result = (sum / 10) + (sum % 10);
		result = ((sum % 10) * 10) + (result % 10);
		sum = result;
		count++;
	} while (result != n);

	cout << count << endl;
	return 0;
}*/