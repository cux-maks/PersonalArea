
## 문제
#### 8진수로 입력된 정수 1개를 10진수로 바꾸어 출력해보자.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%o", &a);
	printf("%d", a);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int n;

	cin >> oct >> n;
	cout << dec << n << endl;

	return 0;

}
```
