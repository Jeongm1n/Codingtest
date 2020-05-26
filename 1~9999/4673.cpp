/*#include<iostream>
using namespace std;
int main() {
	int i = 0, selfnum;
	while (1) {
		for (int j = 0; j <= i; j++) {
			if (j < 100)
				selfnum = j + (j / 10) + (j % 10);
			else if (j >= 100 && j < 1000)
				selfnum = j + (j / 100) + ((j % 100) / 10) + ((j % 100) % 10);
			else if (j >= 1000 && j < 10000)
				selfnum = j + (j / 1000) + ((j % 1000) / 100) + (((j% 1000) % 100) / 10) + (((j % 1000) % 100) % 10);
			if (selfnum == i)
				break;
			else if (j == i)
				cout << i << endl;
		}
		i++;
		if (i > 10000)
			break;
	}
	return 0;
}*/