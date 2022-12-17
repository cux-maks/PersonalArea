
## 문제
#### 정수 1개를 입력받아 2배 곱해 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);
	printf("%d", a<<1);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int n;

	cin >> n;
	cout << (n << 1) << endl;

	return 0;

}
```
