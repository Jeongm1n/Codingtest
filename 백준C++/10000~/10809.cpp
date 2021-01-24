/*#include<iostream>
using namespace std;
int main() {
	char str[100];
	char alpha[26] = { 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' };
	int count[26];
	cin >> str;
	for (int i = 0; i < 26; i++) {
		for (int j = 0; str[j]; j++) {
			if (alpha[i] == str[j]) {
				count[i] = j;
				break;
			}
			else
				count[i] = -1;
		}

	}
	for (int i = 0; i < 26; i++)
		cout << count[i] << " ";
	return 0;
}*/