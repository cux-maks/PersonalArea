
## 문제
#### 입력된 정수의 부호를 바꿔 출력해보자.
#### 단, -2147483647 ~ +2147483647 범위의 정수가 입력된다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a;
	scanf("%d", &a);
	printf("%d", -a);
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
	cout << -1 * n << endl;

	return 0;

}
```
