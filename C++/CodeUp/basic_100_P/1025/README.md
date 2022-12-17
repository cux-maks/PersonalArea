1025
## 문제
#### 다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int num, dec = 10000;
	scanf("%d", &num);
	for (int i = 0; i < 5; i++) {
		printf("[%d]\n", num / dec * dec);
		num = num - num / dec * dec;
		dec = dec / 10;
		
	}
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int num, a;

	cin >> num;

	a = num / 10000;
	cout << "[" << a * 10000 << "]" << endl;

	num = num % 10000;
	a = num / 1000;
	cout << "[" << a * 1000 << "]" << endl;

	num = num % 1000;
	a = num / 100;
	cout << "[" << a * 100 << "]" << endl;

	num = num % 100;
	a = num / 10;
	cout << "[" << a * 10 << "]" << endl;

	num = num % 10;
	a = num;
	cout << "[" << a * 1 << "]" << endl;


	return 0;
}
```
