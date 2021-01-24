/*#include<iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	for (int i = 1; i < n; i++) {
		for (int j = n - i - 1; j >= 0; j--)
			cout << " ";
		cout << "*";
		for (int k = 1; k <= i * 2 - 3; k++) {
			cout << " ";
		}
		if (i == 1) {
			cout << endl;
			continue;
		}
		cout << "*";
		cout << endl;
	}
	for (int i = 1; i <= n * 2 - 1; i++)
		cout << "*";
	cout << endl;
	return 0;
}*/