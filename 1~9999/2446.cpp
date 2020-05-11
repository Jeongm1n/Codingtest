/*#include<iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j < i; j++)
			cout << " ";
		for (int k = (n - i) * 2; k >= 0; k--)
			cout << "*";
		cout << endl;
	}
	for (int i = 1; i < n; i++) {
		for (int j = n - i - 1; j >= 1; j--)
			cout << " ";
		for (int k = 1; k <= i * 2 + 1; k++)
			cout << "*";
		cout << endl;
	}
	return 0;
}*/