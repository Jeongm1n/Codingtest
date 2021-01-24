/*#include<iostream>
using namespace std;
int main() {
	int arr[10];
	int remainder[10];
	int count = 10;
	for (int i = 0; i < 10; i++) {
		cin >> arr[i];
		remainder[i] = arr[i] % 42;
	}
	for (int i = 0; i < 10; i++) {
		int cnt = 0;
		for (int j = i; j < 10; j++) {
			if (remainder[i] == remainder[j])
				cnt++;
		}
		if (cnt > 1)
			count--;
	}
	cout << count << endl;
	return 0;
}*/