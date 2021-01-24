/*#include<iostream>
using namespace std;
int main() {
	int a, b, c, mul = 0;
	int arr[10] = { 0 };
	cin >> a >> b >> c;
	mul = a * b * c;
	while (mul != 0) {
		arr[mul % 10] += 1;
		mul /= 10;
	}
	for (int i = 0; i < 10; i++)
		cout << arr[i] << endl;
	return 0;
}*/