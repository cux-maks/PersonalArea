
## 문제
#### 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
#### 단 0 <= a, b <= 2147483647, b는 0이 아니다.

###### \<c\>
```c
#include <stdio.h>

int main() {

	long long int a, b;
	scanf("%lld %lld", &a, &b);
	printf("%lld\n%lld\n%lld\n%lld\n%lld\n%.2f", a+b, a-b, a*b, a/b, a%b, (float)a/(float)b);
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
	cout << a - b << endl;
	cout << a * b << endl;
	cout << a / b << endl;
	cout << a % b << endl;

	cout.precision(2);
	cout << fixed << (float)a/b << endl;

}
```
