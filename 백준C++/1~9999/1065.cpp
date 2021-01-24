/*#include<iostream>
using namespace std;
int main() {
	int n, index, result=0;
	cin >> n;
	
	for (int i = 1; i <= n; i++) {
		if (i < 100) {
			result++;
			continue;
		}
		else {
			if ((i / 100) - ((i % 100) / 10) == ((i % 100) / 10) - ((i % 100) % 10)) {
				result++;
				continue;
			}
		}
	}
	cout << result << endl;
	return 0;
}*/