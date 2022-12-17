1023
## 문제
#### 실수 1개를 입력받아 정수 부분과 실수 부분으로 나누어 출력한다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a, b;
	scanf("%d.%d", &a, &b);
	printf("%d\n%d", a, b);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>
#include <string>

using namespace std;

int main() {

	string front, back;

	getline(cin, front, '.');
	getline(cin, back);

	cout << front << endl << back << endl;

	return 0;

}
```
