/*#include<iostream>
using namespace std;
int main() {
	int n, temp;
	float sum, count;
	float* size;
	cin >> n;
	size = new float[n];
	int** arr;
	arr = new int* [n];
	for (int i = 0; i < n; i++) {
		cin >> size[i];
		temp = size[i];
		arr[i] = new int[temp];
		for (int j = 0; j < size[i]; j++)
			cin >> arr[i][j];
	}
	for (int i = 0; i < n; i++) {
		count = 0;
		sum = 0;
		for (int j = 0; j < size[i]; j++) {
			sum += arr[i][j];
		}
		sum /= size[i];
		if (sum == 100)
			count = size[i];
		for (int k = 0; k < size[i]; k++) {
			if (arr[i][k] > sum)
				count++;
		}
		sum = count / size[i] * 100;
		cout.setf(ios::showpoint);
		cout.precision(5);
		cout << sum << "%" << endl;
	}
	delete[]arr;
	delete[]size;
	return 0;
}*/