
## 문제
#### 1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때
#### 반대로 출력하는 프로그램을 작성해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);
	printf("%d", !a);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int a;

	cin >> a;

	if (a == 1) {
		cout << 0 << endl;
	}
	else {
		cout << 1 << endl;
	}

	return 0;

}
```
