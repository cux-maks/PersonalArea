
## 문제
#### 16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%x", &a);
	printf("%o", a);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int n;

	cin >> hex >> n;
	cout << oct << n << endl;

	return 0;

}
```
