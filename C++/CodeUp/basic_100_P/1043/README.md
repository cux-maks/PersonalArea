
## 문제
#### 정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.
#### 단, 0 <= a, b <= +2147483647, b는 0이 아니다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	int a, b;
	scanf("%d %d", &a, &b);
	printf("%d", a % b);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	int a, b;

	cin >> a >> b;
	cout << a % b << endl;

	return 0;

}
```
