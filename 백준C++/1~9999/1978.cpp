#include<iostream>
using namespace std;
int main() {
	int n, result=0;
	int* arr;
	cin >> n;
	arr = new int[n];
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	for (int i = 0; i <n; i++) {
		int count = 0;
		for (int j = 2; j <= arr[i]; j++) {
			if (arr[i] % j == 0)
				count++;
		}
		if (count == 1)
			result++;
	}
	cout << result << endl;
	return 0;
}