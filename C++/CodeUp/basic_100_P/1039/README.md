
## 문제
#### 정수 2개를 입력받아 합을 출력해보자.
#### 단, 입력되는 정수는 -2147483648 ~ +2147483648 이다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	long long int a, b;
	scanf("%lld %lld", &a, &b);
	printf("%lld", a + b);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	long long int a, b;

	cin >> a >> b;
	cout << a + b << endl;

	return 0;

}
```
