/*#include<iostream>
using namespace std;
int main() {
	int arr[5], set, minset;
	for (int i = 0; i < 5; i++)
		cin >> arr[i];
	minset = arr[0] + arr[3] - 50;
	for (int i = 0; i < 3; i++) {
		for (int j = 3; j < 5; j++) {
			set = arr[i] + arr[j] - 50;
			if (minset > set)
				minset = set;
		}
	}
	cout << minset << endl;
	return 0;
}*/