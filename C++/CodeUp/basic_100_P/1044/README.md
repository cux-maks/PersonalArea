
## 문제
#### 정수를 1개 입력받아 1만큼 더해 출력해보자.
#### 단, -2147483648 ~ +2147483647 의 범위로 입력된다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	long long int a;
	scanf("%lld", &a);
	printf("%lld", a + 1);
	return 0;

}
```

###### \<c++\>
```c++
#include <iostream>

using namespace std;

int main() {

	long long int n;

	cin >> n;
	cout << n + 1 << endl;

	return 0;

}
```
