/*#include<iostream>
using namespace std;
int main() {
	int n;
	char** str;
	int* score;
	cin >> n;
	str = new char*[n];
	score = new int[n];
	for (int i = 0; i < n; i++)
		str[i] = new char[80];
	for (int i = 0; i < n; i++)
		cin >> str[i];
	for (int i = 0; i < n; i++) {
		int count = 0;
		score[i] = 0;
		for (int j = 0; str[i][j]; j++) {
			if (str[i][j] == 'X')
				count = 0;
			if (str[i][j] == 'O')
				count++;
			score[i] += count;
		}
		cout << score[i] << endl;
	}
	delete[]str;
	delete[]score;
	return 0;
}*/