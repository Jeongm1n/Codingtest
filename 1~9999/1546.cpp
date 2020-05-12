/*#include<iostream>
using namespace std;
int main() {
	int n, max;
	float sum = 0;
	float* arr;
	cin >> n;
	arr = new float[n];
	for (int i = 0; i < n; i++)
		cin >> arr[i];
	max = arr[0];
	for (int i = 0; i < n; i++) {
		if (max < arr[i])
			max = arr[i];
	}
	for (int i = 0; i < n; i++) {
		arr[i] = arr[i] / max * 100;
		sum += arr[i];
	}
	cout << sum / n << endl;
	delete[]arr;
	return 0;
}*/