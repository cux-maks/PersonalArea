
## 문제
#### 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
#### 0 <= a <= 10, 0 <= b <= 10

###### \<c\>
```c
#include <stdio.h>

int main() {

	long long int a, b;
	scanf("%lld %lld", &a, &b);
	printf("%lld", a << b);
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
	cout << (a << b) << endl;

	return 0;

}
```
