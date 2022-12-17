
## 문제
#### 두 개의 참(1) 또는 거짓(0)이 입력될 때,
#### 모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a&&b);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int a, b, c;

	cin >> a >> b;
	
	if (a == 1 && b == 1) {
		cout << 1 << endl;
	}
	else {
		cout << 0 << endl;
	}

	return 0;

}
```
