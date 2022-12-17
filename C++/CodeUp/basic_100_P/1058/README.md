
## 문제
#### 두 개의 참(1) 또는 거짓(0)이 입력될 때,
#### 모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", (a == 0) && (a == b));
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	double a, b, c;

	cin >> a >> b;

	c = (!a&&!b);

	cout << c << endl;

	return 0;

}
```
