/*#include<iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= i; j++)
			cout << "*";
		for (int k = ((n * 2) - (i * 2)); k >= 1; k--)
			cout << " ";
		for (int l = 1; l <= i; l++)
			cout << "*";
		cout << endl;
	}
	for (int i = 1; i < n; i++) {
		for (int j = n-1; j >= i; j--)
			cout << "*";
		for (int k = 1; k <= i * 2; k++)
			cout << " ";
		for (int l = n - 1; l >= i; l--)
			cout << "*";
		cout << endl;
	}
	return 0;
}*/